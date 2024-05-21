import unittest
import pygame
from unittest.mock import Mock

# Initialize pygame modules
pygame.init()

# Mocking the player class
class MockPlayer:
    head = (600, 400)
    cosin = 1
    sin = 0

# Import the peluru class
from peluru import peluru, screen_width, screen_height

class TestPeluru(unittest.TestCase):
    def setUp(self):
        # Setup a display for rendering (necessary for some pygame functionalities)
        self.window = pygame.display.set_mode((screen_width, screen_height))
        self.mock_player = MockPlayer()
        self.peluru_instance = peluru()

        # Mock the player attributes
        self.peluru_instance.point = self.mock_player.head
        self.peluru_instance.x, self.peluru_instance.y = self.mock_player.head
        self.peluru_instance.cosin = self.mock_player.cosin
        self.peluru_instance.sin = self.mock_player.sin
        self.peluru_instance.xv = self.peluru_instance.cosin * 10
        self.peluru_instance.yv = self.peluru_instance.sin * 10

    def test_peluru_initialization(self):
        self.assertEqual(self.peluru_instance.x, self.mock_player.head[0])
        self.assertEqual(self.peluru_instance.y, self.mock_player.head[1])
        self.assertEqual(self.peluru_instance.width, 5)
        self.assertEqual(self.peluru_instance.height, 5)
        self.assertEqual(self.peluru_instance.cosin, self.mock_player.cosin)
        self.assertEqual(self.peluru_instance.sin, self.mock_player.sin)
        self.assertEqual(self.peluru_instance.xv, self.mock_player.cosin * 10)
        self.assertEqual(self.peluru_instance.yv, self.mock_player.sin * 10)

    def test_move(self):
        initial_x = self.peluru_instance.x
        initial_y = self.peluru_instance.y
        self.peluru_instance.move()
        self.assertEqual(self.peluru_instance.x, initial_x + self.peluru_instance.xv)
        self.assertEqual(self.peluru_instance.y, initial_y - self.peluru_instance.yv)

    def test_batasRenderPeluru(self):
        self.peluru_instance.x = screen_width + 1
        self.assertTrue(self.peluru_instance.batasRenderPeluru())

        self.peluru_instance.x = -51
        self.assertTrue(self.peluru_instance.batasRenderPeluru())

        self.peluru_instance.y = screen_height + 1
        self.assertTrue(self.peluru_instance.batasRenderPeluru())

        self.peluru_instance.y = -51
        self.assertTrue(self.peluru_instance.batasRenderPeluru())

        self.peluru_instance.x = screen_width // 2
        self.peluru_instance.y = screen_height // 2
        self.assertFalse(self.peluru_instance.batasRenderPeluru())

    def test_draw(self):
        try:
            self.peluru_instance.draw(self.window)
        except Exception as e:
            self.fail(f"peluru.draw() raised {e} unexpectedly!")

if __name__ == '__main__':
    unittest.main()

# Quit pygame modules
pygame.quit()
