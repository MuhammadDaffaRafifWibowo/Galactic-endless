import unittest
import pygame
import math

# Initialize pygame modules
pygame.init()

# Import the player class
from player import player, screen_width, screen_height

class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Setup a display for rendering (necessary for some pygame functionalities)
        self.window = pygame.display.set_mode((screen_width, screen_height))
        self.player_instance = player

    def test_player_initialization(self):
        self.assertIsInstance(self.player_instance.img, pygame.Surface)
        self.assertEqual(self.player_instance.width, self.player_instance.img.get_width())
        self.assertEqual(self.player_instance.height, self.player_instance.img.get_height())
        self.assertEqual(self.player_instance.x, screen_width // 2)
        self.assertEqual(self.player_instance.y, screen_height // 2)
        self.assertEqual(self.player_instance.sudut, 0)
        self.assertAlmostEqual(self.player_instance.cosin, math.cos(math.radians(90)))
        self.assertAlmostEqual(self.player_instance.sin, math.sin(math.radians(90)))
        self.assertEqual(self.player_instance.head, (self.player_instance.x + self.player_instance.cosin * self.player_instance.width // 2, self.player_instance.y - self.player_instance.sin * self.player_instance.height // 2))

    def test_putarKiri(self):
        initial_sudut = self.player_instance.sudut
        self.player_instance.putarKiri()
        self.assertEqual(self.player_instance.sudut, initial_sudut + 5)
        self.assertAlmostEqual(self.player_instance.cosin, math.cos(math.radians(self.player_instance.sudut + 90)))
        self.assertAlmostEqual(self.player_instance.sin, math.sin(math.radians(self.player_instance.sudut + 90)))

    def test_putarKanan(self):
        initial_sudut = self.player_instance.sudut
        self.player_instance.putarKanan()
        self.assertEqual(self.player_instance.sudut, initial_sudut - 5)
        self.assertAlmostEqual(self.player_instance.cosin, math.cos(math.radians(self.player_instance.sudut + 90)))
        self.assertAlmostEqual(self.player_instance.sin, math.sin(math.radians(self.player_instance.sudut + 90)))

    def test_maju(self):
        initial_x = self.player_instance.x
        initial_y = self.player_instance.y
        self.player_instance.maju()
        self.assertAlmostEqual(self.player_instance.x, initial_x + self.player_instance.cosin * 6)
        self.assertAlmostEqual(self.player_instance.y, initial_y - self.player_instance.sin * 6)

    def test_batasRenderPlayer(self):
        self.player_instance.x = screen_width + 51
        self.player_instance.batasRenderPlayer()
        self.assertEqual(self.player_instance.x, 0)

        self.player_instance.x = -self.player_instance.width - 1
        self.player_instance.batasRenderPlayer()
        self.assertEqual(self.player_instance.x, screen_width)

        self.player_instance.y = -51
        self.player_instance.batasRenderPlayer()
        self.assertEqual(self.player_instance.y, screen_height)

        self.player_instance.y = screen_height + 51
        self.player_instance.batasRenderPlayer()
        self.assertEqual(self.player_instance.y, 0)

    def test_draw(self):
        try:
            self.player_instance.draw(self.window)
        except Exception as e:
            self.fail(f"player.draw() raised {e} unexpectedly!")

if __name__ == '__main__':
    unittest.main()

# Quit pygame modules
pygame.quit()
