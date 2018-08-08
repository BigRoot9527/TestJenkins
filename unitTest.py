# coding: utf-8
import unittest
class Calculator:
    def Add(self, a, b): return a+b - 1

class TestCalculator(unittest.TestCase):
    def test1(self):
        cal = Calculator()
        self.assertEqual(cal.Add(10,10),20)
    def test2(self):
        cal = Calculator()
        self.assertEqual(cal.Add(0,10),10)
    def test3(self):
        cal = Calculator()
        self.assertEqual(cal.Add(10,0),10)

if __name__ == '__main__':
    unittest.main()
