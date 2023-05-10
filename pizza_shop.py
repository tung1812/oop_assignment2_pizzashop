# TODO Claim this as your own work by modifying the following...
# File: pizza_shop.py 
# Author: Nguyen Son Tung
# Id: 43185
# Description: your program description...
# This is my own work as defined by the Academic Integrity policy. 
import math
import copy
import os

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
        self.__price = price
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
            return (self.getName() == other.getName()) and (self.getPrice() == other.getPrice())
        else: 
            return False
    def __repr__(self):
        return f"name: {self.__name}, price: {self.__price}$"

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

    def scaleCost(self, diameter):
        costPerSquareInch = self.costPerSquareInch()
        self.__diameter = diameter
        newPrice = costPerSquareInch * math.pi * (diameter / 2)**2
        self.setPrice(newPrice)

    def setSize(self, size):
        if size == "small":
            self.scaleCost(10)
        elif size == "medium":
            self.scaleCost(12)
        elif size == "large":
            self.scaleCost(14)
        else:
            raise ValueError("Must be one of Small, Medium, Large")

    def __str__(self):
        return f"{self.getName()}, {self.__diameter} inch, ${self.getPrice():.2f}"



class Pizza(Food):
    def __init__(self, name, price, base, toppings):
        super().__init__(name, price)
        self.originalBase = base.clone()
        self.currentBase = None
        self.originalToppings = [t.clone() for t in toppings]
        self.currentToppings = [t.clone() for t in toppings]

    def addTopping(self, topping):
        self.currentToppings.append(topping.clone())

    def removeTopping(self, topping):
        self.currentToppings = [t for t in self.currentToppings if not t.equalCheck(topping)]

    def getPrice(self):
        price = super().getPrice()
        if self.currentBase is not None:
            price += self.currentBase.getPrice() - self.originalBase.getPrice()

        for topping in self.currentToppings:
            if not any(topping.equalCheck(originalTopping) for originalTopping in self.originalToppings):
                price += topping.getPrice()

        for topping in self.originalToppings:
            if not any(topping.equalCheck(currentTopping) for currentTopping in self.currentToppings):
                price -= topping.getPrice()

        return price
    
    def clone(self):
        if isinstance(self, Pizza):
            return type(self)(self.getName(), self.getPrice(), self.originalBase, self.originalToppings)
        else:
            raise TypeError('Cannot clone object of different class')

    def equalCheck(self, other):
        if not isinstance(other, Pizza):
            return False
        if self.getName() != other.getName():
            return False
        if self.currentBase is not None and not self.currentBase.equalCheck(other.currentBase):
            return False
        if len(self.currentToppings) != len(other.currentToppings):
            return False
        for topping1, topping2 in zip(self.currentToppings, other.currentToppings):
            if not topping1.equalCheck(topping2):
                return False
        return True

    def __str__(self):
        return f"Name: {self.getName()} price: {self.getPrice()} base: {self.currentBase} toppings: {self.currentToppings}"

class PizzaShop:
    def __init__(self):
        self.ingredients = []
        self.menu = []

    def load_ingredients(self):
        with open(os.path.join('files', 'ingredients.txt')) as file:
            for line in file:
                line = line.strip()
                if line.startswith('base:'):
                    name, price = line[5:].strip().split('$')
                    base = PizzaBase(name.strip(), 0, float(price))
                    self.menu.append(base)
                else:
                    name, price = line.strip().split('$')
                    ingredient = Food(name.strip(), float(price))
                    self.ingredients.append(ingredient)

        # Read the menu from menu.txt
    def load_menu(self):
        pizzas = []
        with open('menu.txt', 'r') as f:
            for line in f:
                parts = line.strip().split('$')
                name = parts[0]
                price = float(parts[1])
                base, *toppings = parts[2].split(', ')
                pizzas.append(Pizza(name, price, base, toppings))
        return pizzas

    

def main():
    # TODO Write your main program code here...
    print("~~ Welcome to the Pizza Shop ~~")
    # pizzaBase1 = PizzaBase('thin crust', 12, 10)
    # print(pizzaBase1.costPerSquareInch())
    # print(pizzaBase1.getPrice())
    # pizzaBase1.scaleCost(14)
    # print(pizzaBase1.getPrice())
    # print(pizzaBase1.clone().getDiameter())
    # base = PizzaBase('thin crust', 12, 10)
    # chicken = Food('chicken', 4)
    # onion = Food('onion', 1)
    # mush = Food('mushroom', 4)
    # spin = Food('spinach', 3)
    # toppings = [chicken, onion, mush]
    # p1 = Pizza('Meat lovers', 20, base, toppings)
    # print(p1.getPrice())
    # p1.addTopping(spin)
    # print(p1)
    # print(p1.getPrice())
    # p1.removeTopping(mush)
    # print(p1)
    # print(p1.getPrice())
    # p2 = p1.clone()
    # print(p2)
    # print(p1.equalCheck(p2))
    

    



# WARNING: Do not write any code in global scope

if __name__ == '__main__':
    main()