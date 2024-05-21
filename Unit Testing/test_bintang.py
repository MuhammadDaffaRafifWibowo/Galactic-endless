import unittest
import pygame
import random

# Initialize pygame modules
pygame.init()

# Import the bintang class
from bintang import bintang, screen_width, screen_height

class TestBintang(unittest.TestCase):
    def setUp(self):
        # Setup a display for rendering (necessary for some pygame functionalities)
        self.window = pygame.display.set_mode((screen_width, screen_height))
        self.bintang_instance = bintang()  # Inisialisasi objek bintang

    def test_bintang_initialization(self):
        self.assertIsInstance(self.bintang_instance.img, pygame.Surface)
        self.assertEqual(self.bintang_instance.width, self.bintang_instance.img.get_width())
        self.assertEqual(self.bintang_instance.height, self.bintang_instance.img.get_height())
        self.assertIn(self.bintang_instance.spawnPoint, [
            (self.bintang_instance.x, self.bintang_instance.y) for _ in range(10)
        ])

    def test_bintang_direction_and_velocity(self):
        self.assertIn(self.bintang_instance.xdir, [-1, 1])
        self.assertIn(self.bintang_instance.ydir, [-1, 1])
        self.assertEqual(self.bintang_instance.xv, self.bintang_instance.xdir * 2)
        self.assertEqual(self.bintang_instance.yv, self.bintang_instance.ydir * 2)

    def test_draw(self):
        try:
            self.bintang_instance.draw(self.window)
        except Exception as e:
            self.fail(f"bintang.draw() raised {e} unexpectedly!")

if __name__ == '__main__':
    unittest.main()

# Quit pygame modules
pygame.quit()
