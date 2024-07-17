import unittest
from analysis.forgetting_curve import ForgettingCurve
from datetime import datetime

class TestForgettingCurve(unittest.TestCase):
    def setUp(self):
        self.commits = [
            {'commit': {'author': {'date': '2024-01-01T00:00:00Z'}}},
            {'commit': {'author': {'date': '2024-01-05T00:00:00Z'}}},
            {'commit': {'author': {'date': '2024-01-10T00:00:00Z'}}}
        ]
        self.forgetting_curve = ForgettingCurve(self.commits)

    def test_calculate_curve(self):
        curve = self.forgetting_curve.calculate_curve()
        self.assertEqual(len(curve), 2)

if __name__ == '__main__':
    unittest.main()
