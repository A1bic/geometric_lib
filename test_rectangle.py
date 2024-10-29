import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    '''
    Тесты для area()
    '''

    #Базовые тесты
    def test_area_basic(self):
        self.assertEqual(area(10, 8), 40)
        self.assertEqual(area(5, 90), 225)
        self.assertEqual(area(18, 16), 144)
        self.assertEqual(area(8, 13), 52)


    #Тестирование с нулями
    def test_area_zero(self):
        self.assertEqual(area(0, 0), 0)
        self.assertEqual(area(23, 0), 0)
        self.assertEqual(area(0, 987), 0)

    #Тестирование граничных чисел
    def test_area_limit_value(self):
        self.assertEqual(area(9999999, 1234567), 9999999 * 1234567 / 2)
        self.assertEqual(area(0.00001, 0.000001), 0.00001 * 0.000001 / 2)
        self.assertEqual(area(9999999, 0.000001), 9999999 * 0.000001 / 2)
        self.assertIsInstance(area(1e18, 1e18), float)
        self.assertIsInstance(area(1e18 ** -1, 1e18 ** -1), float)


    '''
    Тесты для perimeter()
    '''

    #Базовые тесты
    def test_perimeter_basic(self):
        self.assertEqual(perimeter(10, 89, 67), 166)
        self.assertEqual(perimeter(47, 6, 321), 374)
        self.assertEqual(perimeter(1, 98, 100), 199)
        self.assertEqual(perimeter(5, 56, 4), 65)

    #Тестирование с нулями
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0)
        
    #Тестирование граничных чисел
    def testperimeter_limit_value(self):
        self.assertEqual(perimeter(9999999, 7654321, 1234567), 9999999 + 7654321 + 1234567)
        self.assertEqual(perimeter(0.00001, 0.002, 0.000000001), 0.00001 + 0.002 + 0.000000001)
        self.assertIsInstance(perimeter(1e10, 1e10, 1e10), float)
        self.assertIsInstance(perimeter(1e18 ** -1, 1e18 ** -1, 1e18 ** -1), float)

    '''
    Проверка типов данных
    '''
    def test_type_errors(self):
        with self.assertRaises(TypeError):
            area("5", "90")
            area("5", 90)
            area(5, "90")

        with self.assertRaises(ValueError):
            area(-8, 16)

        with self.assertRaises(TypeError):
            perimeter("5", "4", "3")
            perimeter(5, "4", "3")
            perimeter("5", 4, 3)

        with self.assertRaises(ValueError):
            perimeter(-8, 3, 9)
