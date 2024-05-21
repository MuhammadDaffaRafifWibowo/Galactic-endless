import unittest
import pygame
import random
import math

# Initialize pygame modules
pygame.init()

# Import the ally class
from ally import ally, screen_width, screen_height

class TestAlly(unittest.TestCase):
    def setUp(self):
        # Setup a display for rendering (necessary for some pygame functionalities)
        self.window = pygame.display.set_mode((screen_width, screen_height))

    def test_ally_initialization(self):
        test_ally = ally()
        self.assertIsInstance(test_ally.img, pygame.Surface)
        self.assertEqual(test_ally.width, test_ally.img.get_width())
        self.assertEqual(test_ally.height, test_ally.img.get_height())
        self.assertIn(test_ally.spawnPoint, [
            (test_ally.x, test_ally.y) for _ in range(10)
        ])

    def test_ally_direction_and_velocity(self):
        test_ally = ally()
        self.assertIn(test_ally.xdir, [-1, 1])
        self.assertIn(test_ally.ydir, [-1, 1])
        self.assertIn(test_ally.xv, [-2, -1, 1, 2])
        self.assertIn(test_ally.yv, [-2, -1, 1, 2])

    def test_ally_angle_calculation(self):
        test_ally = ally()
        expected_angle = math.degrees(math.atan2(test_ally.xv, -test_ally.yv))
        self.assertAlmostEqual(test_ally.angle, expected_angle, places=5)

    def test_ally_draw(self):
        test_ally = ally()
        try:
            test_ally.draw(self.window)
        except Exception as e:
            self.fail(f"ally.draw() raised {e} unexpectedly!")

if __name__ == '__main__':
    unittest.main()

# Quit pygame modules
pygame.quit()
