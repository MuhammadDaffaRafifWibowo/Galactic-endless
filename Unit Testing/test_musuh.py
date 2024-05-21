import unittest
import pygame
import random

# Initialize pygame modules
pygame.init()

# Import the classes
from musuh import Musuh, Ufo, MegaUfo, screen_width, screen_height

class TestMusuh(unittest.TestCase):
    def setUp(self):
        # Setup a display for rendering (necessary for some pygame functionalities)
        self.window = pygame.display.set_mode((screen_width, screen_height))

    def test_ufo_initialization(self):
        ufo = Ufo()
        self.assertEqual(ufo.jenis, 1)
        self.assertEqual(ufo.width, 50)
        self.assertEqual(ufo.height, 50)
        self.assertIsInstance(ufo.img, pygame.Surface)
        self.assertIn(ufo.spawnPoint, [
            (ufo.x, ufo.y) for _ in range(10)
        ])

    def test_megaufo_initialization(self):
        mega_ufo = MegaUfo()
        self.assertEqual(mega_ufo.jenis, 2)
        self.assertEqual(mega_ufo.width, 100)
        self.assertEqual(mega_ufo.height, 100)
        self.assertIsInstance(mega_ufo.img, pygame.Surface)
        self.assertIn(mega_ufo.spawnPoint, [
            (mega_ufo.x, mega_ufo.y) for _ in range(10)
        ])

    def test_ufo_direction_and_velocity(self):
        ufo = Ufo()
        self.assertIn(ufo.xdir, [-1, 1])
        self.assertIn(ufo.ydir, [-1, 1])
        self.assertIn(ufo.xv, [-1, 1])
        self.assertIn(ufo.yv, [-1, 1])

    def test_megaufo_direction_and_velocity(self):
        mega_ufo = MegaUfo()
        self.assertIn(mega_ufo.xdir, [-1, 1])
        self.assertIn(mega_ufo.ydir, [-1, 1])
        self.assertIn(mega_ufo.xv, [-2, -1, 1, 2])
        self.assertIn(mega_ufo.yv, [-2, -1, 1, 2])

    def test_ufo_draw(self):
        ufo = Ufo()
        try:
            ufo.draw(self.window)
        except Exception as e:
            self.fail(f"Ufo.draw() raised {e} unexpectedly!")

    def test_megaufo_draw(self):
        mega_ufo = MegaUfo()
        try:
            mega_ufo.draw(self.window)
        except Exception as e:
            self.fail(f"MegaUfo.draw() raised {e} unexpectedly!")

if __name__ == '__main__':
    unittest.main()

# Quit pygame modules
pygame.quit()
