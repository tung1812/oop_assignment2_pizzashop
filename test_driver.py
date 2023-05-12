# TODO Claim this as your own work by modifying the following...
# File: test_driver.py 
# Author: Nguyen Son Tung  
# Id: 43185
# Description: your program description here... 
# This is my own work as defined by the 
# Academic Integrity policy. 

from pizza_shop import *
import unittest

class TestPizzaBase(unittest.TestCase):

    def testClone(self):
        pb1 = PizzaBase("thin crust", 8.99)
        pb2 = pb1.clone()
        self.assertEqual(pb1.getName(), pb2.getName())
        self.assertEqual(pb1.getPrice(), pb2.getPrice())
        self.assertEqual(pb1.getDiameter(), pb2.getDiameter())

        f = Food("ham", 2)
        # Test with dangerous argument
        with self.assertRaises(TypeError):
            pb3 = pb1.clone(f)

    def testEqualCheck(self):
        pb1 = PizzaBase("thin crust", 8.99)
        pb2 = PizzaBase("thin crust", 8.99)
        pb3 = PizzaBase("cheese crust", 9.99)

        self.assertTrue(pb1.equalCheck(pb2))
        self.assertFalse(pb1.equalCheck(pb3))
        with self.assertRaises(TypeError):
            pb1.equalCheck("not a pizza")

    def testCostPerSquareInch(self):
        pb1 = PizzaBase("thin crust", 8.99)
        self.assertAlmostEqual(pb1.costPerSquareInch(), 0.058, places=3)

        with self.assertRaises(ValueError):
            pb2 = PizzaBase("cheese crust", -9)
            pb2.costPerSquareInch()

    def testScaleCost(self):
        pb1 = PizzaBase("thin crust", 8.99)
        pb1.scaleCost(10)
        self.assertAlmostEqual(pb1.getPrice(), 4.58, places=1)

        with self.assertRaises(ValueError):
            pb2 = PizzaBase("cheese crust", -9.99)
            pb2.scaleCost(20)

    def testSetSize(self):
        pb1 = PizzaBase("thin crust", 8.99)
        pb1.setSize("small")
        self.assertAlmostEqual(pb1.getPrice(), 4.58, places=1)

        with self.assertRaises(ValueError):
            pb2 = PizzaBase("cheese crust", 9.99)
            pb2.setSize("extra large")


        
if __name__ == "__main__":
    unittest.main()