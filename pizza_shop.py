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
        return self.__price
    def setPrice(self, price):
        return price
    def getStrPrice(self):
        return f"${self.__price:.2f}"
    
    def clone(self):
        # return Food(self.__name, self.__price)
        if isinstance(self, Food):
            return type(self)(self.__name, self.__price)
        else:
            raise TypeError("Cannot clone object of different class")
    def equalCheck(self, other):
        if isinstance(other, Food):
            return (self.__name == other.__name) and (self.__price == other.__price)
        else: 
            return False
    def __str__(self):
        return f"name: {self.__name}, price: {self.__price}"

class PizzaBase(Food):
    def __init__(self, name, price, diameter):
        super().__init__(name, price)
        self.__diameter = diameter

    def clone(self):
        # return PizzaBase(self.getName(), self.getPrice(), self.__diameter)
        if isinstance(self, PizzaBase):
            return type(self)(self.getName(), self.getPrice(), self.__diameter)
        else:
            raise TypeError("Cannot clone object of different class")

    def equalCheck(self, other):
        if isinstance(other, PizzaBase):
            return (self.getName() == other.getName()) and (self.getPrice() == other.getPrice()) and (self.__diameter == other.__diameter)

    def costPerSquareInch(self):
        radius = self.__diameter / 2
        return self.getPrice() / (math.pi * radius**2)

    def getDiameter(self):
        return self.__diameter

    def setDiameter(self, diameter):
        costPerSquareInch = self.costPerSquareInch()
        self.__diameter = diameter
        self.setPrice(costPerSquareInch * math.pi * (diameter / 2)**2)

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
        return f"{self.getName()}, {self.__diameter} inch, ${self.getPrice():.2f}"


def main():
    # TODO Write your main program code here...
    print("~~ Welcome to the Pizza Shop ~~")
    pizzaBase1 = PizzaBase('thin crust', 12, 10)
    
    print(pizzaBase1.clone().getDiameter())

    print()



# WARNING: Do not write any code in global scope

if __name__ == '__main__':
    main()