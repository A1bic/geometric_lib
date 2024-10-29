import unittest
from square import area, perimeter

class RectangleTestCase(unittest.TestCase):

    '''
    Тесты для area()
    '''

    #Базовые тесты
    def test_area_basic(self):
        self.assertEqual(area(10), 100)
        self.assertEqual(area(5), 25)
        self.assertEqual(area(18), 324)
        self.assertEqual(area(8), 64)


    #Тестирование с нулями
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    #Тестирование граничных чисел
    def test_area_limit_value(self):
        self.assertEqual(area(9999999), 9999999**2)
        self.assertEqual(area(0.00001), 0.00001**2)
        self.assertIsInstance(area(1e18), float)
        self.assertIsInstance(area(1e18 ** -1), float)

    '''
    Тесты для perimeter()
    '''

    #Базовые тесты
    def test_perimeter_basic(self):
        self.assertEqual(perimeter(10), 40)
        self.assertEqual(perimeter(47), 188)
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(5), 20)

    #Тестирование с нулями
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
        
    #Тестирование граничных чисел
    def testperimeter_limit_value(self):
        self.assertEqual(perimeter(9999999), 39999996)
        self.assertEqual(perimeter(0.00001), 0.00004)
        self.assertIsInstance(perimeter(1e18), float)
        self.assertIsInstance(perimeter(1e18 ** -1), float)
    '''
    Проверка типов данных
    '''
    def test_insert_value_errors(self):
        with self.assertRaises(ValueError):
            area(-10)
        with self.assertRaists(TypeError):
            area("5")
        with self.assertRaises(TypeError):
            perimeter("13")
        with self.assertRaises(ValueError):
            perimeter(-3)
