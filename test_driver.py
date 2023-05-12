# File: test_driver.py 
# Author: Nguyen Son Tung  
# Id: 43185
# Description: a set of unit tests written using the unittest framework in Python. These tests are designed to validate the functionality and behavior of the PizzaBase class from the pizza_shop module.
# This is my own work as defined by the 
# Academic Integrity policy. 

from pizza_shop import *
import unittest

'''Unit tests for the PizzaBase class."""
'''
class TestPizzaBase(unittest.TestCase):

    '''Test the clone method of PizzaBase.
    '''
    def testClone(self):
        # Test with safe argument
        pb1 = PizzaBase("thin crust", 8.99)
        pb2 = pb1.clone()
        self.assertEqual(pb1.getName(), pb2.getName())
        self.assertEqual(pb1.getPrice(), pb2.getPrice())
        self.assertEqual(pb1.getDiameter(), pb2.getDiameter())

        f = Food("ham", 2)
        # Test with dangerous argument
        with self.assertRaises(TypeError):
            pb3 = pb1.clone(f)

    '''Test the equalCheck method of PizzaBase.
    '''
    def testEqualCheck(self):
        # Test with safe argument
        pb1 = PizzaBase("thin crust", 8.99)
        pb2 = PizzaBase("thin crust", 8.99)
        pb3 = PizzaBase("cheese crust", 9.99)

        self.assertTrue(pb1.equalCheck(pb2))
        self.assertFalse(pb1.equalCheck(pb3))
        # Test with dangerous argument
        with self.assertRaises(TypeError):
            pb1.equalCheck("not a pizza")

    '''Test the costPerSquareInch method of PizzaBase.
    '''
    def testCostPerSquareInch(self):
        # Test with safe argument
        pb1 = PizzaBase("thin crust", 8.99)
        self.assertAlmostEqual(pb1.costPerSquareInch(), 0.058, places=3)

        # Test with dangerous argument
        with self.assertRaises(ValueError):
            pb2 = PizzaBase("cheese crust", -9)
            pb2.costPerSquareInch()

    '''Test the scaleCost method of PizzaBase.
    '''
    def testScaleCost(self):
        # Test with safe argument
        pb1 = PizzaBase("thin crust", 8.99)
        pb1.scaleCost(10)
        self.assertAlmostEqual(pb1.getPrice(), 4.58, places=1)
        # Test with dangerous argument
        with self.assertRaises(ValueError):
            pb2 = PizzaBase("cheese crust", -9.99)
            pb2.scaleCost(20)

    '''Test the setSize method of PizzaBase.
    '''
    def testSetSize(self):
        # Test with safe argument
        pb1 = PizzaBase("thin crust", 8.99)
        pb1.setSize("small")
        self.assertAlmostEqual(pb1.getPrice(), 4.58, places=1)
        # Test with dangerous argument
        with self.assertRaises(ValueError):
            pb2 = PizzaBase("cheese crust", 9.99)
            pb2.setSize("extra large")


        
if __name__ == "__main__":
    unittest.main()