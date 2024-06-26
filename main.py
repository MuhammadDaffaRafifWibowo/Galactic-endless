import pygame
import random
import sys
from player import player
from peluru import peluru
from musuh import Ufo, MegaUfo
from ally import ally 
from bintang import bintang
from button import Button

pygame.init()
pygame.mixer.init()

class MainMenu:
    def __init__(self, game):
        self.game = game
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 800))
        pygame.display.set_caption("Menu")
        self.bg = pygame.image.load("Assets/mainmenu/mainmenubg.jpg")
        self.clock = pygame.time.Clock()
        self.background_music = pygame.mixer.Sound("Assets/Sound/ObservingTheStar.ogg")  # Load background music
        self.background_music.set_volume(0.7)  # Set the volume

    def get_font(self, size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("Assets/mainmenu/font.ttf", size)

    def play_background_music(self):
        self.background_music.play(-1)  # Play the background music indefinitely (-1)

    def stop_background_music(self):
        self.background_music.stop()  # Stop the background music

    def main_menu(self):
        self.play_background_music()  # Start playing background music
        while True:
            self.screen.blit(self.bg, (0, 0))
            menu_mouse_pos = pygame.mouse.get_pos()

            menu_text = self.get_font(78).render("GALACTIC ENDLESS", True, "#0250a3")
            menu_rect = menu_text.get_rect(center=(640, 170))

            play_button = Button(image=pygame.image.load("Assets/mainmenu/Play Rect.png"), pos=(640, 350),
                                text_input="PLAY", font=self.get_font(60), base_color="#d7fcd4", hovering_color="White")
            quit_button = Button(image=pygame.image.load("Assets/mainmenu/Quit Rect.png"), pos=(640, 650),
                                text_input="QUIT", font=self.get_font(60), base_color="#d7fcd4", hovering_color="White")
            credit_button = Button(image=pygame.image.load("Assets/mainmenu/Credit Rect.png"), pos=(640, 500),
                                text_input="CREDIT", font=self.get_font(60), base_color="#d7fcd4", hovering_color="White")

            self.screen.blit(menu_text, menu_rect)

            for button in [play_button, quit_button, credit_button]:
                button.changeColor(menu_mouse_pos)
                button.scaleUp(menu_mouse_pos)  # Apply the scale up effect on hover
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop_background_music()  # Stop background music before quitting
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(menu_mouse_pos):
                        self.stop_background_music()  # Stop background music before starting the game
                        self.game.start()
                    if quit_button.checkForInput(menu_mouse_pos):
                        self.stop_background_music()  # Stop background music before quitting
                        pygame.quit()
                        sys.exit()
                    if credit_button.checkForInput(menu_mouse_pos):
                        self.show_credit()

            pygame.display.update()
            self.clock.tick(60)

    def show_credit(self):
           while True:
                menu_mouse_pos = pygame.mouse.get_pos()

                self.screen.blit(self.bg, (0, 0))

                credits = [
                    "1. Nur Afni Daem Miarti",
                    "2. Muhammad Daffa Rafif Wibowo",
                    "3. Faris Pratama",
                    "4. Rafelina Octa Ladelavia",
                    "5. Adin Adry Tjindarbumi",
                    "6. Nasywa Talitha Heryanna"
                ]

                y_offset = 260
                for credit in credits:
                    menu_text = self.get_font(36).render(credit, True, (255, 255, 255))
                    CREDIT_RECT = menu_text.get_rect(center=(640, y_offset))
                    self.screen.blit(menu_text, CREDIT_RECT)
                    y_offset += 40  # Adjust the offset for each line

                CREDIT_BACK = Button(image=None, pos=(640, 700), 
                                    text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")

                CREDIT_BACK.changeColor(menu_mouse_pos)
                CREDIT_BACK.update(self.screen)

                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if CREDIT_BACK.checkForInput(menu_mouse_pos):
                            return  # Keluar dari fungsi
                        
                pygame.display.update()

class Game:
    def __init__(self, width, height):
        self.screen_width = width
        self.screen_height = height

        # Background yang digunakan
        self.background = pygame.image.load('Assets/Map/map.png')

        # Asset sound effect yang digunakan 
        self.shoot = pygame.mixer.Sound("Assets/Sound/SHOOT011.mp3")
        self.shoot.set_volume(.25)
        self.explosion = pygame.mixer.Sound("Assets/Sound/SFX_Explosion_02.mp3")
        self.explosion.set_volume(.25)

       
        # Display judul game
        pygame.display.set_caption('Galactic Endless')
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.clock = pygame.time.Clock()

        # Variabel yang diperlukan untuk permainan
        self.Gameover = False
        self.nyawa = 3
        self.score = 0
        self.machineGun = False
        self.highScore = 0

        # Inisialisasi variabel yang digunakan untuk fungsi
        self.playerPeluru = []
        self.musuhlist = []
        self.allylist = []
        self.bntglist = [bintang()]
        self.count = 0
        self.mgStart = -1

    def redrawGamewindow(self):
        self.window.blit(self.background, (0, 0))
        # Menambah teks untuk menampilkan nyawa pemain
        self.font = pygame.font.SysFont('Verdana', 30)
        self.nyawaTeks = self.font.render('Nyawa: ' + str(self.nyawa), 1, (255, 255, 255))
        self.replayTeks = self.font.render('Tekan Tab untuk Bermain Kembali', 1, (255, 255, 255))
        self.scoreTeks = self.font.render('Skor: ' + str(self.score), 1, (255, 255, 255))
        self.highScoreTeks = self.font.render('Skor Tertinggi: ' + str(self.highScore), 1, (255, 255, 255))
        # Penempatan posisi teks nyawa
        self.window.blit(self.nyawaTeks, (25, 25))
        self.window.blit(self.scoreTeks, (self.screen_width - self.scoreTeks.get_width() - 25, 25))
        self.window.blit(self.highScoreTeks, (self.screen_width - self.highScoreTeks.get_width() - 25, 25 + self.scoreTeks.get_height()))
        # Menampilkan teks bermain kembali apabila gameover
        if self.Gameover:
            self.window.blit(self.replayTeks, (self.screen_width // 2 - self.replayTeks.get_width() // 2, self.screen_height // 2 - self.replayTeks.get_height() // 2))
        # Menampilkan pemain di layar
        player.draw(self.window)
        # Menampilkan musuh di layar
        for m in self.musuhlist:
            m.draw(self.window)
        # Menampilkan peluru di layar
        for i in self.playerPeluru:
            i.draw(self.window)
        # Menampilkan ally di layar
        for a in self.allylist:
            a.draw(self.window)
        # Menampilkan bintang di layar
        for w in self.bntglist:
            w.draw(self.window)

        if self.machineGun:
            pygame.draw.rect(self.window, (0, 0, 0), [self.screen_width // 2 - 51, 19, 102, 22])
            pygame.draw.rect(self.window, (255, 255, 255), [self.screen_width // 2 - 50, 20, 100 - 100 * (self.count - self.mgStart) / 500, 20])

        pygame.display.update()

    def start(self):
        run = True

        # Background music gameplay
        pygame.mixer.music.load("Assets/Sound/Space Sprinkles.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)


        while run:
            self.clock.tick(60)
            self.count += 1

            if not self.Gameover:
                if self.count % 75 == 0:
                    ran = random.choice([1, 1, 1, 2])
                    if ran == 1:
                        self.musuhlist.append(Ufo())
                    else:
                        self.musuhlist.append(MegaUfo())

                if self.count % 150 == 0:
                    self.allylist.append(ally())

                if self.count % 1000 == 0:
                    self.bntglist.append(bintang())

                player.batasRenderPlayer()

                for i in self.playerPeluru:
                    i.move()
                    if i.batasRenderPeluru():
                        self.playerPeluru.pop(self.playerPeluru.index(i))

                for m in self.musuhlist:
                    m.x += m.xv
                    m.y += m.yv

                    # Mengecek apakah musuh menabrak player
                    if (player.x >= m.x and player.x <= m.x + m.width) or (player.x + player.width >= m.x and player.x + player.width <= m.x + m.width):
                        if (player.y > m.y and player.y <= m.y + m.height) or (player.y + player.height >= m.y and player.y + m.height <= m.y + m.height):
                            self.explosion.play()
                            self.nyawa -= 1
                            self.musuhlist.pop(self.musuhlist.index(m))
                            break

                    # Hit peluru
                    for p in self.playerPeluru:
                        if (p.x >= m.x and p.x <= m.x + m.width) or (p.x + p.width >= m.x and p.x + p.width <= m.x + m.width):
                            if (p.y >= m.y and p.y <= m.y + m.height) or (p.y + p.height >= m.y and p.y + p.height <= m.y + m.height):
                                if m.jenis == 2:
                                    self.explosion.play()
                                    self.score += 30
                                    nm1 = Ufo()
                                    nm2 = Ufo()
                                    nm1.x = m.x
                                    nm2.x = m.x
                                    nm1.y = m.y
                                    nm2.y = m.y
                                    self.musuhlist.append(nm1)
                                    self.musuhlist.append(nm2)
                                else:
                                    self.explosion.play()
                                    self.score += 15

                                self.musuhlist.pop(self.musuhlist.index(m))
                                self.playerPeluru.pop(self.playerPeluru.index(p))
                                break

                for a in self.allylist:
                    a.x += a.xv
                    a.y += a.yv

                    if (player.x >= a.x and player.x <= a.x + a.width) or (player.x + player.width >= a.x and player.x + player.width <= a.x + a.width):
                        if (player.y > a.y and player.y <= a.y + a.height) or (player.y + player.height >= a.y and player.y + a.height <= a.y + a.height):
                            self.explosion.play()
                            self.nyawa -= 1
                            if self.score >= 15:
                                self.score -= 15
                            else:
                                self.score = 0
                            self.allylist.pop(self.allylist.index(a))
                            break

                    for p in self.playerPeluru:
                        if (p.x >= a.x and p.x <= a.x + a.width) or (p.x + p.width >= a.x and p.x + p.width <= a.x + a.width):
                            if (p.y >= a.y and p.y <= a.y + a.height) or (p.y + p.height >= a.y and p.y + p.height <= a.y + a.height):
                                self.explosion.play()
                                if self.score >= 15:
                                    self.score -= 15
                                else:
                                    self.score = 0
                                self.allylist.pop(self.allylist.index(a))
                                self.playerPeluru.pop(self.playerPeluru.index(p))
                                break

                for w in self.bntglist:
                    w.x += w.xv
                    w.y += w.yv
                    if (player.x >= w.x and player.x <= w.x + w.width) or (player.x + player.width >= w.x and player.x + player.width <= w.x + w.width):
                        if (player.y > w.y and player.y <= w.y + w.height) or (player.y + player.height >= w.y and player.y + w.height <= w.y + w.height):
                            self.bntglist.pop(self.bntglist.index(w))
                            break
                    for p in self.playerPeluru:
                        if (p.x >= w.x and p.x <= w.x + w.width) or (p.x + p.width >= w.x and p.x + p.width <= w.x + w.width):
                            if (p.y >= w.y and p.y <= w.y + w.height) or (p.y + p.height >= w.y and p.y + p.height <= w.y + w.height):
                                self.machineGun = True
                                self.mgStart = self.count
                                self.bntglist.pop(self.bntglist.index(w))
                                self.playerPeluru.pop(self.playerPeluru.index(p))
                                break

                if self.nyawa <= 0:
                    self.Gameover = True

                if self.mgStart != -1:
                    if self.count - self.mgStart > 500:
                        self.machineGun = False
                        self.mgStart = -1

                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    player.putarKiri()
                if keys[pygame.K_RIGHT]:
                    player.putarKanan()
                if keys[pygame.K_UP]:
                    player.maju()
                if keys[pygame.K_SPACE]:
                    if self.machineGun:
                        self.playerPeluru.append(peluru())
                        self.shoot.play()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not self.Gameover:
                            if not self.machineGun:
                                self.playerPeluru.append(peluru())
                                self.shoot.play()

                    if event.key == pygame.K_TAB:
                        if self.Gameover:
                            self.Gameover = False
                            self.nyawa = 3
                            self.musuhlist.clear()
                            self.allylist.clear()
                            self.bntglist.clear()
                            if self.score > self.highScore:
                                self.highScore = self.score
                            self.score = 0

            self.redrawGamewindow()
        pygame.quit()

if __name__ == "__main__":
    game = Game(width=1200, height=800)
    menu = MainMenu(game)
    menu.main_menu()
