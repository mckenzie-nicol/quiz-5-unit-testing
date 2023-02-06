from unittest import TestCase

from calculate_pay import calculate_pay

class TestCalculatePay(TestCase):
    def test_zero_hours(self):
        self.assertEqual(0, calculate_pay(0, 10.00))

    def test_zero_pay(self):
        self.assertEqual(0, calculate_pay(40, 0.00))

    def test_negative_hour(self):
        self.assertEqual(0, calculate_pay(-50, 25.00))
