import unittest
from task_234 import f4, f5, sp1

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.test_numbers = sp1

    # Тесты для функции f4()
    def test_f4_with_sp1(self):
        self.assertEqual(f4(self.test_numbers), "Нечетные")

    def test_f4_all_even(self):
        self.assertEqual(f4([2, 4, 6]), "Четные")

    def test_f4_all_odd(self):
        self.assertEqual(f4([1, 3, 5]), "Нечетные")

    def test_f4_mixed(self):
        self.assertEqual(f4([2, 1]), "Четные")

    def test_f4_empty(self):
        self.assertEqual(f4([]), "Нечетные")

    # Тесты для функции f5()
    def test_f5_zero(self):
        self.assertEqual(f5(0), 1)

    def test_f5_one(self):
        self.assertEqual(f5(1), 1)

    def test_f5_five(self):
        self.assertEqual(f5(5), 120)

    def test_f5_three(self):
        self.assertEqual(f5(3), 6)


if __name__ == '__main__':
    unittest.main()