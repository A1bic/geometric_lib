import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    '''
    Тесты для area()
    '''

    #Базовые тесты
    def test_area_basic(self):
        with self.subTest("Regular Test 1"):
            self.assertEqual(area(4), 50.26548245743669)
        with self.subTest("Regular Test 2"):
            self.assertEqual(area(145), 66051.9855417254)
        with self.subTest("Regular Test 3"):
            self.assertEqual(area(12), 452.3893421169302)
        


    #Тестирование с нулями
    def test_area_zero(self):
        with self.subTest("Zero Test"):
            self.assertEqual(area(0), 0)

    #Тестирование граничных чисел
    def test_area_limit_value(self):
        with self.subTest("Big number Test"):
            self.assertEqual(area(12345678), 478828248493921.5)
        with self.subTest("Small number Test"):
            self.assertEqual(area(0.01), 0.00031415926535897936)
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
            self.assertEqual(perimeter(5), 31.41592653589793)
        with self.subTest("Regular Test 2"):
            self.assertEqual(perimeter(234), 1470.2653618800232)
        with self.subTest("Regular Test 3"):
            self.assertEqual(perimeter(12), 75.39822368615503)

    #Тестирование с нулями
    def test_perimeter_zero(self):
        with self.subTest("Zero Test"):
            self.assertEqual(perimeter(0), 0)
        
    #Тестирование граничных чисел
    def testperimeter_limit_value(self):
        with self.subTest("Big number Test"):
            self.assertEqual(perimeter(87654321), 550748341.818003)
        with self.subTest("Small number Test"):
            self.assertEqual(perimeter(0.0001), 0.0006283185307179586)
        with self.subTest("Very big number type Test"):
            self.assertIsInstance(perimeter(1e18), float)
        with self.subTest("Very small number type Test"):
            self.assertIsInstance(perimeter(1e18 ** -1), float)


    '''
    Проверка вводимых данных
    '''
    def test_insert_value_errors(self):
        with self.subTest("TypeError Area Test"):
            with self.assertRaises(TypeError):
                area("5")
        
        with self.subTest("ValueError Area Test"):
            with self.assertRaises(ValueError):
                area(-3)

        with self.subTest("TypeError Perimeter Test"):
            with self.assertRaises(TypeError):
                perimeter("4")

        with self.subTest("ValueError Perimeter Test"):
            with self.assertRaises(ValueError):
                perimeter(-5)

