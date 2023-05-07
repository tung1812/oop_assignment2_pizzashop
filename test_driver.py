# TODO Claim this as your own work by modifying the following...
# File: test_driver.py 
# Author: Nguyen Son Tung  
# Id: 43185
# Description: your program description here... 
# This is my own work as defined by the 
# Academic Integrity policy. 

from pizza_shop import PizzaBase
import unittest

class TestPizzaBase(unittest.TestCase):

    def testClone(self):
        pb1 = PizzaBase("thin crust", 8.99, 12)
        pb2 = pb1.clone()
        self.assertEqual(pb1.getName(), pb2.getName())
        self.assertEqual(pb1.getPrice(), pb2.getPrice())
        self.assertEqual(pb1.getDiameter(), pb2.getDiameter())

        with self.assertRaises(AttributeError):
            pb3 = pb1.clone(1)

    def testEqualCheck(self):
        pb1 = PizzaBase("thin crust", 8.99, 12)
        pb2 = PizzaBase("thin crust", 8.99, 12)
        pb3 = PizzaBase("cheese crust", 9.99, 14)

        self.assertTrue(pb1.equalCheck(pb2))
        self.assertFalse(pb1.equalCheck(pb3))
        with self.assertRaises(AttributeError):
            pb1.equalCheck("not a pizza")

    def testCostPerSquareInch(self):
        pb1 = PizzaBase("thin crust", 8.99, 12)
        self.assertAlmostEqual(pb1.costPerSquareInch(), 0.198, places=3)

        with self.assertRaises(ZeroDivisionError):
            pb2 = PizzaBase("cheese crust", 0, 12)
            pb2.costPerSquareInch()

    def testGetDiameter(self):
        pb1 = PizzaBase("thin crust", 8.99, 12)
        self.assertEqual(pb1.getDiameter(), 12)

        with self.assertRaises(AttributeError):
            pb2 = PizzaBase("cheese crust", 9.99, 14)
            pb2.getDiameter()

    def testSetDiameter(self):
        pb1 = PizzaBase("thin crust", 8.99, 12)
        pb1.setDiameter(10)
        self.assertAlmostEqual(pb1.getPrice(), 6.37, places=2)

        with self.assertRaises(ValueError):
            pb2 = PizzaBase("cheese crust", 9.99, 14)
            pb2.setDiameter(20)

    def testSetSize(self):
        pb1 = PizzaBase("thin crust", 8.99, 12)
        pb1.setSize("small")
        self.assertAlmostEqual(pb1.getPrice(), 3.99, places=2)

        with self.assertRaises(ValueError):
            pb2 = PizzaBase("cheese crust", 9.99, 14)
            pb2.setSize("extra large")

    def testStr(self):
        pb1 = PizzaBase("thin crust", 8.99, 12)
        self.assertEqual(str(pb1), "thin crust, 12 inch, $8.99")

        with self.assertRaises(AttributeError):
            pb2 = PizzaBase("cheese crust", 9.99, 14)
            str(pb2)

        
if __name__ == "__main__":
    unittest.main()