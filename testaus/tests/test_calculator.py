import unittest
import calculator.calculator as calculator
# from .. import plus, minus


class TestCalculator(unittest.TestCase):

    def test_plus_numbers_returns_sum_of_integers(self):
        result = calculator.plus(2, 3)
        self.assertEqual(result, 5)

    def test_plus_numbers_works_with_negative_numbers(self):
        result = calculator.plus(-2, -3)
        self.assertEqual(result, -5)

    def test_plus_numbers_returns_sum_of_floats(self):
        result = calculator.plus(2.4, 3.2)
        self.assertEqual(result, 5.6)

    def test_plus_numbers_returns_sum_of_integer_and_float(self):
        result = calculator.plus(2, 3.2)
        self.assertEqual(result, 5.2)

    def test_plus_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(TypeError):
            calculator.plus(1, "a")
                            

if __name__ == '__main__':
    unittest.main()