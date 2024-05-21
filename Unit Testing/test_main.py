import unittest
from unittest.mock import patch, Mock, MagicMock
import pygame
import sys

# Mocking necessary classes and methods
from main import Game, MainMenu, Button  # Sesuaikan dengan path yang benar

class TestGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.game = Game(width=1200, height=800)
        self.window = pygame.display.set_mode((1200, 800))

    def test_game_initialization(self):
        self.assertEqual(self.game.screen_width, 1200)
        self.assertEqual(self.game.screen_height, 800)
        self.assertEqual(self.game.nyawa, 3)
        self.assertEqual(self.game.score, 0)
        self.assertFalse(self.game.Gameover)

    def test_redraw_game_window(self):
        try:
            self.game.redrawGamewindow()
        except Exception as e:
            self.fail(f"redrawGamewindow raised {e} unexpectedly!")

    @patch('pygame.display.set_mode')
    @patch('pygame.display.set_caption')
    def test_game_start(self, mock_set_caption, mock_set_mode):
        with patch('pygame.event.get', side_effect=[[pygame.event.Event(pygame.QUIT)]]):
            with patch('pygame.mixer.music.load'), patch('pygame.mixer.music.set_volume'), patch('pygame.mixer.music.play'):
                try:
                    self.game.start()
                except SystemExit:
                    pass  # We expect a SystemExit due to pygame.quit()

class TestMainMenu(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.mock_game = Mock()
        self.main_menu = MainMenu(self.mock_game)

    def test_main_menu_initialization(self):
        self.assertEqual(self.main_menu.screen.get_size(), (1280, 800))
        self.assertIsInstance(self.main_menu.bg, pygame.Surface)
        self.assertIsInstance(self.main_menu.background_music, pygame.mixer.Sound)

    @patch.object(MainMenu, 'play_background_music')
    @patch.object(MainMenu, 'stop_background_music')
    @patch('pygame.mouse.get_pos')
    @patch('pygame.event.get')
    @patch('pygame.display.update')
    def test_main_menu(self, mock_update, mock_event_get, mock_get_pos, mock_stop_music, mock_play_music):
        mock_get_pos.return_value = (0, 0)
        mock_event_get.return_value = [pygame.event.Event(pygame.QUIT)]
        
        # Creating a separate instance of Clock and mocking its tick method
        with patch.object(pygame.time, 'Clock', return_value=MagicMock(tick=Mock())) as mock_clock:
            try:
                self.main_menu.main_menu()
            except SystemExit:
                pass  # We expect a SystemExit due to pygame.quit()
        
        mock_play_music.assert_called_once()
        mock_stop_music.assert_called_once()

if __name__ == '__main__':
    unittest.main()

# Quit pygame modules
pygame.quit()
