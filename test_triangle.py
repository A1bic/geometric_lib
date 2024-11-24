import unittest
from triangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    '''
    Тесты для area()
    '''

    #Базовые тесты
    def test_area_basic(self):
        with self.subTest("Regular Test 1"):
            self.assertEqual(area(10, 8), 40)
        with self.subTest("Regular Test 2"):
            self.assertEqual(area(5, 90), 225)
        with self.subTest("Regular Test 3"):
            self.assertEqual(area(18, 16), 144)
        with self.subTest("Regular Test 4"):
            self.assertEqual(area(8, 13), 52)


    #Тестирование с нулями
    def test_area_zero(self):
        with self.subTest("Zero Test 1"):
            self.assertEqual(area(0, 0), 0)
        with self.subTest("Zero Test 2"):
            self.assertEqual(area(23, 0), 0)
        with self.subTest("Zero Test 3"):
            self.assertEqual(area(0, 987), 0)

    #Тестирование граничных чисел
    def test_area_limit_value(self):
        with self.subTest("Big numbers Test"):
            self.assertEqual(area(9999999, 1234567), 9999999 * 1234567 / 2)
        with self.subTest("Small numbers Test"):
            self.assertEqual(area(0.00001, 0.000001), 0.00001 * 0.000001 / 2)
        with self.subTest("Bit and Small numbers Test"):
            self.assertEqual(area(9999999, 0.000001), 9999999 * 0.000001 / 2)
        with self.subTest("Very big numbers type Test"):
            self.assertIsInstance(area(1e18, 1e18), float)
        with self.subTest("Very small numbers type Test"):
            self.assertIsInstance(area(1e18 ** -1, 1e18 ** -1), float)


    '''
    Тесты для perimeter()
    '''

    #Базовые тесты
    def test_perimeter_basic(self):
        with self.subTest("Regular Test 1"):
            self.assertEqual(perimeter(10, 89, 67), 166)
        with self.subTest("Regular Test 2"):
            self.assertEqual(perimeter(47, 6, 321), 374)
        with self.subTest("Regular Test 3"):
            self.assertEqual(perimeter(1, 98, 100), 199)
        with self.subTest("Regular Test 4"):
            self.assertEqual(perimeter(5, 56, 4), 65)

    #Тестирование с нулями
    def test_perimeter_zero(self):
        with self.subTest("Zero Test"):
            self.assertEqual(perimeter(0, 0, 0), 0)
        
    #Тестирование граничных чисел
    def testperimeter_limit_value(self):
        with self.subTest("Big number Test"):
            self.assertEqual(perimeter(9999999, 7654321, 1234567), 9999999 + 7654321 + 1234567)
        with self.subTest("Small number Test"):
            self.assertEqual(perimeter(0.00001, 0.002, 0.000000001), 0.00001 + 0.002 + 0.000000001)
        with self.subTest("Very big number type Test"):
            self.assertIsInstance(perimeter(1e10, 1e10, 1e10), float)
        with self.subTest("Very small number type Test"):
            self.assertIsInstance(perimeter(1e18 ** -1, 1e18 ** -1, 1e18 ** -1), float)

    '''
    Проверка типов данных
    '''
    def test_type_errors(self):
        with self.assertRaises(TypeError):
            with self.subTest("TypeError Area Test 1"):
                area("5", "90")
            with self.subTest("TypeError Area Test 2"):
                area("5", 90)
            with self.subTest("TypeError Area Test 3"):
                area(5, "90")

        with self.assertRaises(ValueError):
            with self.subTest("ValueError Area Test"):
                area(-8, 16)

        with self.assertRaises(TypeError):
            with self.subTest("TypeError Perimeter Test 1"):
                perimeter("5", "4", "3")
            with self.subTest("TypeError Perimeter Test 2"):
                perimeter(5, "4", "3")
            with self.subTest("TypeError Perimeter Test 3"):
                perimeter("5", 4, 3)

        with self.assertRaises(ValueError):
            with self.subTest("ValueError Perimeter Test"):
                perimeter(-8, 3, 9)
