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
            return (self.__name == other.__name) and (self.__price == other.__price)
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
        self.currentBase = base.clone()
        self.originalToppings = [t.clone() for t in toppings]
        self.currentToppings = [t.clone() for t in toppings]

    def addTopping(self, topping):
        self.currentToppings.append(topping.clone())

    def removeTopping(self, topping):
        if topping in self.currentToppings:
            self.currentToppings.remove(topping)

    def getPrice(self):
        price = self.currentBase.getPrice() - self.originalBase.getPrice()
        for topping in self.currentToppings:
            if topping not in self.originalToppings:
                price += topping.getPrice()
        return price

    def clone(self):
        if isinstance(self, Pizza):
            return type(self)(self.getName(), self.originalBase, self.originalToppings)
        else:
            raise TypeError('Cannot clone object of different class')

    def equalCheck(self, other):
        if not isinstance(other, Pizza):
            return False
        if self.getName() != other.getName():
            return False
        if not self.currentBase.equals(other.currentBase):
            return False
        if len(self.currentToppings) != len(other.currentToppings):
            return False
        for topping1, topping2 in zip(self.currentToppings, other.currentToppings):
            if not topping1.equals(topping2):
                return False
        return True

    def __str__(self):
        return f"Name: {self.getName()} price: {self.getPrice()} base: {self.currentBase} toppings: {self.currentToppings}"

class PizzaShop:
    def __init__(self):
        self.ingredients = {}
        self.menu = {}

        with open(os.path.join('files', 'ingredients.txt')) as file:
            for line in file:
                name, price = line.strip().split(',')
                self.ingredients[name] = float(price)

        with open(os.path.join('files', 'menu.txt')) as file:
            for line in file:
                name, base_name, topping_names = line.strip().split('|')
                base = PizzaBase(base_name, self.ingredients[base_name])
                toppings = [Topping(name, self.ingredients[name]) for name in topping_names.split(',')]
                pizza = Pizza(name, base, toppings)
                self.menu[name] = pizza

    def displayMenu(self):
        print("Menu:")
        for name, pizza in self.menu.items():
            print(name, "-", pizza.get_price())

    def orderPizza(self, name):
        if name not in self.menu:
            print("Sorry, we don't have that pizza.")
            return
        pizza = self.menu[name].clone()
        while True:
            print(pizza)
            print("Options:")
            print("1. Add topping")
            print("2. Remove topping")
            print("3. Confirm order")
            choice = input("Enter an option number: ")
            if choice == "1":
                topping_name = input("Enter topping name: ")
                if topping_name in self.ingredients:
                    topping = Topping(topping_name, self.ingredients[topping_name])
                    pizza.add_topping(topping)
                else:
                    print("Sorry, we don't have that topping.")
            elif choice == "2":
                topping_name = input("Enter topping name: ")
                toppings = [t.name for t in pizza.currentToppings]
                if topping_name in toppings:
                    topping = Topping(topping_name, self.ingredients[topping_name])
                    pizza.remove



def main():
    # TODO Write your main program code here...
    print("~~ Welcome to the Pizza Shop ~~")
    # pizzaBase1 = PizzaBase('thin crust', 12, 10)
    # print(pizzaBase1.costPerSquareInch())
    # print(pizzaBase1.getPrice())
    # pizzaBase1.scaleCost(14)
    # print(pizzaBase1.getPrice())
    # print(pizzaBase1.clone().getDiameter())
    ogBase = PizzaBase('thin crust', 12, 10)
    currentBase = PizzaBase('chese crust', 13, 14)
    chicken = Food('chicken', 4)
    onion = Food('onion', 1)
    mush = Food('mushroom', 2.5)
    spin = Food('spinach', 3)
    ogToppings = [chicken, onion, mush]
    currentToppings = [chicken, onion, spin]
    p1 = Pizza('Meat lovers', 20, ogBase, ogToppings)
    p1.addTopping(spin)
    print(p1)
    p1.removeTopping(onion)
    print(p1)





# WARNING: Do not write any code in global scope

if __name__ == '__main__':
    main()