import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):

    '''
    Тесты для area()
    '''

    #Базовые тесты
    def test_area_basic(self):
        with self.subTest("Regular Test 1"):
            self.assertEqual(area(10), 100)
        with self.subTest("Regular Test 2"):
            self.assertEqual(area(5), 25)
        with self.subTest("Regular Test 3"):
            self.assertEqual(area(18), 324)
        with self.subTest("Regular Test 4"):
            self.assertEqual(area(8), 64)


    #Тестирование с нулями
    def test_area_zero(self):
        with self.subTest("Zero Test"):
            self.assertEqual(area(0), 0)

    #Тестирование граничных чисел
    def test_area_limit_value(self):
        with self.subTest("Big number Test"):
            self.assertEqual(area(9999999), 9999999**2)
        with self.subTest("Small number Test"):
            self.assertEqual(area(0.00001), 0.00001**2)
        with self.subTest("Very big number type Test"):
            self.assertIsInstance(area(1e18), float)
        with self.subTest("Very small number type Test"):
            self.assertIsInstance(area(1e18 ** -1), float)

    '''
    Тесты для perimeter()
    '''

    #Базовые тесты
    def test_perimeter_basic(self):
        with self.subTest("Regular Test 1"):
            self.assertEqual(perimeter(10), 40)
        with self.subTest("Regular Test 2"):
            self.assertEqual(perimeter(47), 188)
        with self.subTest("Regular Test 3"):
            self.assertEqual(perimeter(1), 4)
        with self.subTest("Regular Test 4"):
            self.assertEqual(perimeter(5), 20)

    #Тестирование с нулями
    def test_perimeter_zero(self):
        with self.subTest("Zero Test"):
            self.assertEqual(perimeter(0), 0)
        
    #Тестирование граничных чисел
    def testperimeter_limit_value(self):
        with self.subTest("Big number Test"):
            self.assertEqual(perimeter(9999999), 39999996)
        with self.subTest("Small number Test"):
            self.assertEqual(perimeter(0.00001), 0.00004)
        with self.subTest("Very big number type Test"):
            self.assertIsInstance(perimeter(1e18), float)
        with self.subTest("Very small number type Test"):
            self.assertIsInstance(perimeter(1e18 ** -1), float)
    '''
    Проверка типов данных
    '''
    def test_insert_value_errors(self):
        with self.subTest("TypeError Area Test"):
            with self.assertRaises(ValueError):
                area(-10)
        with self.subTest("ValueError Area Test"):
            with self.assertRaists(TypeError):
                area("5")
        with self.subTest("TypeError Perimeter Test"):
            with self.assertRaises(TypeError):
                perimeter("13")
        with self.subTest("ValueError Perimeter Test"):
            with self.assertRaises(ValueError):
                perimeter(-3)
