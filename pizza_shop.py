# File: pizza_shop.py 
# Author: Nguyen Son Tung
# Id: 43185
# Description: your program description...
# This is my own work as defined by the Academic Integrity policy. 
import math
import os



class Food:
    '''Initializes a new instance of the Food class.
    '''
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def getName(self):
        return self.__name
    def getPrice(self):
        return self.__price
    
    def setPrice(self, price):
        self.__price = price
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
    ''' This represents the round base that the Pizza ingredients are added to.
    '''
    def __init__(self, name, price):
        '''Initialises the PizzaBase attributes including name, price and diameter
        '''
        super().__init__(name, price)
        self.__diameter = 14


    def getDiameter(self):
        return self.__diameter

    def clone(self):
        if isinstance(self, PizzaBase):
            return type(self)(self.getName(), self.getPrice())
        else:
            raise TypeError("Cannot clone object of different class")

    def equalCheck(self, other):
        if isinstance(other, PizzaBase):
            return (
                self.getName() == other.getName()
                and self.getPrice() == other.getPrice())
        else:
            raise TypeError("Wrong type of object")


    def costPerSquareInch(self):
        if self.getPrice() < 0:
            raise ValueError("Invalid price: price cannot be negative")
        radius = self.__diameter / 2
        return self.getPrice() / (math.pi * radius ** 2)

    def scaleCost(self, diameter):
        costPerSquareInch = self.costPerSquareInch()
        self.__diameter = diameter
        newPrice = costPerSquareInch * math.pi * (diameter / 2)**2
        self.setPrice(newPrice)

    def setSize(self, size):
        if size == "small":
            # self.setDiameter(10)
            self.scaleCost(10)
        elif size == "medium":
            # self.setDiameter(12)
            self.scaleCost(12)
        elif size == "large":
            # self.setDiameter(14)
            self.scaleCost(14)
        else:
            raise ValueError("Must be one of Small, Medium, Large")
    def getSize(self):
        if self.__diameter == 10:
            return "small"
        if self.__diameter == 12:
            return "medium"
        if self.__diameter == 14:
            return "large"
        
    def __str__(self):
        if self.__diameter is None:
            return f"{self.getName()}, diameter: Unknown, ${self.getPrice():.2f}"
        else:
            return f"{self.getSize()}, {self.getName()}, ${self.getPrice():.2f}"


class Pizza(Food):
    def __init__(self, name, price, base, toppings):
        super().__init__(name, price)
        self.originalBase = base.clone()
        self.currentBase = None
        self.originalToppings = []
        for t in toppings:
            self.originalToppings.append(t.clone())
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

        return float(price)
    
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
        toppings_str = (' ' * 4) + (', ').join(topping.getName() for topping in self.currentToppings)
        if self.currentBase is None:
            return f"Your Pizza: {self.getName()} {self.originalBase.getSize()} {self.originalBase.getName()} ${self.getPrice()}\n{toppings_str}"
        else:
            return f"Your Pizza: {self.getName()} {self.currentBase.getSize()} {self.currentBase.getName()} ${self.getPrice()}\n{toppings_str}"


    
    
class PizzaShop:
    def __init__(self):
        self.ingredients = []
        self.menu = []
        self.orderHistory = []
    def loadIngredients(self):
        with open(os.path.join('files', 'ingredients.txt')) as file:
            for line in file:
                line = line.strip()
                if line.startswith('base:'):
                    name, price = line[5:].strip().split('$')
                    base = PizzaBase(name.strip(), float(price))
                    self.ingredients.append(base)
                else:
                    name, price = line.strip().split('$')
                    ingredient = Food(name.strip(), float(price))
                    self.ingredients.append(ingredient)

    def loadMenu(self):
        with open(os.path.join('files', 'menu.txt'), 'r') as file:
            for line in file:
                name = line[0 : line.index("$") - 1]
                price = line[line.index("$")+1 : line.index("$") + 3]
                toppingStr = line[line.index("$") + 4 : len(line) - 1]
                toppings = toppingStr.split(',' + ' ')
                toppings_food = []
                for i in range(len(toppings)):
                    for ingredient in self.ingredients:
                        if toppings[i] == ingredient.getName():
                            toppings_food.append(ingredient.clone())

                base = PizzaBase("thin crust", 8)
                pizza = Pizza(name, price, base, toppings_food)
                self.menu.append(pizza)
  

    def orderPizza(self):
        print("Menu:")
        for pizza in self.menu:
            print(f"{pizza.getName()}, {pizza.originalBase.getSize()}, {pizza.originalBase.getName()} ${float(pizza.getPrice()):.2f}:")
            print(" " * 4 + ", ".join(topping.getName() for topping in pizza.currentToppings))

        pizza_choice = input("What pizza would you like: ")
        selected_pizza = None
        found_pizza = False
        for pizza in self.menu:
            if pizza.getName() == pizza_choice:
                selected_pizza = pizza.clone()
                found_pizza = True

        if found_pizza:
            print("Your pizza:")
            print(selected_pizza)
            return selected_pizza.clone()
        else:
            print("We do not make that kind of pizza.")

    def changeSize(self, pizza):
        size_choice = input("What size pizza would you like (small/medium/large):")
        if size_choice in ["small", "medium", "large"]:
            # Create a new instance of the current base with the updated size
            new_base = pizza.originalBase.clone()
            new_base.setSize(size_choice)
            pizza.currentBase = new_base
            print("Your pizza:")
            print(pizza)
            return pizza
        else:
            print("The size must be small/medium/large")
            return None


    def changeBase(self, pizza):
        print("Bases:")
        for ingredient in self.ingredients:
            if isinstance(ingredient, PizzaBase):
                print(ingredient.getName())

        base_choice = input("What base would you like: ")
        base_found = False
        for ingredient in self.ingredients:
            if isinstance(ingredient, PizzaBase) and ingredient.getName() == base_choice:
                pizza.currentBase = ingredient.clone()
                base_found = True

        
        if base_found:
            print("Your pizza:")
            print(pizza)
            return pizza
        else:
            print(f"{base_choice} is not a base.")
            return None

    def addTopping(self, pizza):
        print("Toppings:")
        for ingredient in self.ingredients:
            if not isinstance(ingredient, PizzaBase):
                print(f"{ingredient.getName()} ${ingredient.getPrice():.2f}")

        topping_choice = input("What topping would you like to add: ")
        
        for topping in self.ingredients:
            if not isinstance(topping, PizzaBase) and topping.getName() == topping_choice:
                selected_topping = topping.clone() 

        if selected_topping is not None:
            pizza.addTopping(selected_topping)
            print("Your pizza:")
            print(pizza)
        else:
            print("Invalid topping choice.")
    
    def removeTopping(self, pizza):
        print("Toppings:")
        for topping in pizza.currentToppings:
            print(topping.getName())

        topping_choice = input("What topping would you like to remove: ")
        if topping_choice in [topping.getName() for topping in pizza.currentToppings]:
            topping_choice = topping
            pizza.removeTopping(topping_choice)
            print("Your pizza:")
            print(pizza)
        else:
            print(f"Could not find '{topping_choice}' topping.")

    def displayOrder(self):
        print("So far you have ordered...")
        for pizza in self.orderHistory:
            print(pizza)

    def saveReceipt(self, customer_name):
        receipt_directory_name = os.path.join("files", "receipt")
        if not os.path.exists(receipt_directory_name):
            os.mkdir(receipt_directory_name)
        filename = filename = os.path.join(receipt_directory_name, f"{customer_name}_receipt.txt")

        with open(filename, "w") as file:
            file.write("Receipt:\n")
            for pizza in self.orderHistory:
                file.write(str(pizza) + "\n")
            file.write(f"Enjoy your meal {customer_name}! :)")

    def menu(self):
        pass

def main():
    
    print("~~ Welcome to the Pizza Shop ~~")
    name = input("Please enter your name: ")
    while len(name.split()) < 1:
        name = input("Please enter at least 1 word for your name: ")

    shop = PizzaShop()
    shop.loadIngredients()
    shop.loadMenu()
    # shop.menu()

    
    exit_program = False
    while not exit_program:
        print("1. Order Pizza")
        print("2. Display orders")
        print("3. Exit")
        choice = input("How may I help you: ")

        if choice == '1':
            pizza_choice = shop.orderPizza()
            sub_choice = ''
            while pizza_choice is not None and sub_choice != '6':
                print("Submenu:")
                print("1. Change Size")
                print("2. Change Pizza Base")
                print("3. Add Topping")
                print("4. Remove Topping")
                print("5. Order")
                print("6. Cancel")
                sub_choice = input("What would you like to do: ")
                if sub_choice == '1':
                    # Code for changing size
                    shop.changeSize(pizza_choice)
                elif sub_choice == '2':
                    # Code for changing pizza base
                    shop.changeBase(pizza_choice)
                elif sub_choice == '3':
                    # Code for adding topping
                    shop.addTopping(pizza_choice)
                elif sub_choice == '4':
                    # Code for removing topping
                    shop.removeTopping(pizza_choice)
                elif sub_choice == '5':
                    # Code for placing the order
                    shop.orderHistory.append(pizza_choice)
                    sub_choice = '6'
                elif sub_choice != '6':
                    print("Invalid submenu choice.")

        elif choice == '2':
            print("Displaying orders...")
            # Code to display orders
            shop.displayOrder()

        elif choice == '3':
            shop.saveReceipt(name)
            print(f"Have a good day, {name}! :)")
            exit_program = True

        else:
            print("Please select either 1, 2, or 3.")
#WARNING: Do not write any code in global scope

if __name__ == '__main__':
    main()