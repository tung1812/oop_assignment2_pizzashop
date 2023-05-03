# TODO Claim this as your own work by modifying the following...
# File: pizza_shop.py 
# Author: Nguyen Son Tung
# Id: 43185
# Description: your program description...
# This is my own work as defined by the Academic Integrity policy. 
import math
import copy


# TODO Write your classes here...

class Food:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def getName(self):
        return self.__name
    
    def getPrice(self):
        return f"${self.__price:.2f}"
    
    def clone(self, other):
        if isinstance(other, Food):
            return Food(self.__name, self.__price)
        
    def equalCheck(self, other):
        if isinstance(other, Food):
            return (self.__name == other.__name) and (self.__price == other.__price)
        else: 
            return False

class PizzaBase(Food):
    def __init__(self, name, price, diameter):
        super().__init__(name, price)
        self.__diameter = diameter

    def clone(self, other):
        if isinstance(other, PizzaBase):
            return PizzaBase(self.__name, self.price, self.__diameter)

    def equalCheck(self, other):
        if isinstance(other, PizzaBase):
            return (self.__name == other.__name) and (self.price == other.price) and (self.__diameter == other.__diameter)

    def costPerSquareInch(self):
        radius = self.__diameter / 2
        return self.price / (math.pi * radius**2)

    def setDiameter(self, diameter):
        costPerSquareInch = self.costPerSquareInch()
        self.__diameter = diameter
        self.price = costPerSquareInch * math.pi * (diameter / 2)**2

    def setSize(self, size):
        if size == "small":
            self.setDiameter(10)
        elif size == "medium":
            self.setDiameter(12)
        elif size == "large":
            self.setDiameter(14)
        else:
            raise ValueError("Invalid size")

    def __str__(self):
        return f"{self.__name}, {self.__diameter} inch, ${self.price:.2f}"


def main():
    # TODO Write your main program code here...
    print("~~ Welcome to the Pizza Shop ~~")
    print()



# WARNING: Do not write any code in global scope

if __name__ == '__main__':
    main()