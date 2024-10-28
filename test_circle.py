import unittest
from circle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    '''
    Тесты для area()
    '''

    #Базовые тесты
    def test_area_basic(self):
        self.assertEqual(area(4), 50.26548245743669)
        self.assertEqual(area(145), 66051.9855417254)
        self.assertEqual(area(12), 452.3893421169302)
        


    #Тестирование с нулями
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    #Тестирование граничных чисел
    def test_area_limit_value(self):
        self.assertEqual(area(12345678), 478828248493921.5)
        self.assertEqual(area(0.01), 0.00031415926535897936)



    '''
    Тесты для perimeter()
    '''

    #Базовые тесты
    def test_perimeter_basic(self):
        self.assertEqual(perimeter(5), 31.41592653589793)
        self.assertEqual(perimeter(234), 1470.2653618800232)
        self.assertEqual(perimeter(12), 75.39822368615503)

    #Тестирование с нулями
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
        
    #Тестирование граничных чисел
    def testperimeter_limit_value(self):
        self.assertEqual(perimeter(87654321), 550748341.818003)
        self.assertEqual(perimeter(0.0001), 0.0006283185307179586)

    '''
    Проверка типов данных
    '''
    def test_type_errors(self):
        with self.assertRaises(TypeError):
            area("5")
        with self.assertRaises(TypeError):
            perimeter("4")
        
