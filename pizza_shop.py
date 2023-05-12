# File: pizza_shop.py 
# Author: Nguyen Son Tung
# Id: 43185
# Description: The code represents a simple pizza ordering system implemented using object-oriented programming in Python. It consists of several classes that interact with each other to handle pizza orders, manage ingredients, and generate receipts.
# This is my own work as defined by the Academic Integrity policy. 
import math

'''Represents a generic food item with a name and price.
'''
class Food:

    '''Initializes a new instance of the Food class.
    
        Args:
            name (str): The name of the food item.
            price (float): The price of the food item.
    '''
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    '''Returns the name of the food item.
    
        Returns:
            str: The name of the food item.
    '''
    def getName(self):
        return self.__name
    
    '''Returns the price of the food item.
    
        Returns:
            float: The price of the food item.
    '''
    def getPrice(self):
        return self.__price
    
    '''Sets the price of the food item.
    
        Args:
            price (float): The new price of the food item.
    '''
    def setPrice(self, price):
        self.__price = price

    '''Returns the formatted price of the food item.
    
        Returns:
            str: The formatted price of the food item (e.g., "$10.00").
    '''
    def getStrPrice(self):
        return f"${self.__price:.2f}"
    
    '''Creates a clone of the food item.
    
        Returns:
            Food: A new instance of the same food item class with the same name and price.
        
        Raises:
            TypeError: If the object being cloned is not an instance of the Food class.
    '''
    def clone(self):
        if isinstance(self, Food):
            return type(self)(self.__name, self.__price)  # Create a new instance of the same class with the same name and price
        else:
            raise TypeError("Cannot clone object of different class")
        
    '''Checks if another food item is equal to the current food item.
    
        Args:
            other (Food): The other food item to compare with.

        Returns:
            bool: True if the food items are equal, False otherwise.
    '''
    def equalCheck(self, other):
        if isinstance(other, Food):
            return (self.getName() == other.getName()) and (self.getPrice() == other.getPrice()) # Compare the name and price of the food items
        else: 
            return False
    '''Returns a string representation of the food item.

        Returns:
            str: A string representation of the food item in the format "name: <name>, price: <price>$".
    '''
    def __repr__(self):
        return f"name: {self.__name}, price: {self.__price}$"


''' This represents the round base that the Pizza ingredients are added to.
'''
class PizzaBase(Food):
        
    '''Initialises the PizzaBase attributes including name, price and diameter

        Args:
            name (str): The name of the pizza base.
            price (float): The price of the pizza base.
    '''
    def __init__(self, name, price):
        super().__init__(name, price)
        self.__diameter = 14     # Default diameter is set to 14

    '''Returns the diameter of the pizza base.

        Returns:
            int: The diameter of the pizza base.
    '''
    def getDiameter(self):
        return self.__diameter

    '''Creates a clone of the pizza base.
    
        Returns:
            PizzaBase: A new instance of the PizzaBase class with the same name and price.

        Raises:
            TypeError: If the object being cloned is not an instance of the PizzaBase class.
    '''
    def clone(self):
        if isinstance(self, PizzaBase):
            return type(self)(self.getName(), self.getPrice())  # Create a new instance of the same class with the same name and price
        else:
            raise TypeError("Cannot clone object of different class")

    '''Checks if another pizza base is equal to the current pizza base.
    
        Args:
            other (PizzaBase): The other pizza base to compare with.

        Returns:
            bool: True if the pizza bases are equal, False otherwise.

        Raises:
            TypeError: If the object being compared is not an instance of the PizzaBase class.
    '''
    def equalCheck(self, other):
        if isinstance(other, PizzaBase):
            return (
                self.getName() == other.getName()
                and self.getPrice() == other.getPrice()) # Compare the name and price of the pizza bases
        else:
            raise TypeError("Wrong type of object")

    '''Calculates the cost per square inch of the pizza base.
    
        Returns:
            float: The cost per square inch of the pizza base.

        Raises:
            ValueError: If the price of the pizza base is negative.
    '''
    def costPerSquareInch(self):
        if self.getPrice() < 0:
            raise ValueError("Invalid price: price cannot be negative")
        radius = self.__diameter / 2
        return self.getPrice() / (math.pi * radius ** 2)

    '''Scales the cost of the pizza base based on the new diameter.
    
        Args:
            diameter (int): The new diameter of the pizza base.
    '''
    def scaleCost(self, diameter):
        costPerSquareInch = self.costPerSquareInch()
        self.__diameter = diameter
        newPrice = costPerSquareInch * math.pi * (diameter / 2)**2
        self.setPrice(newPrice)

    '''Sets the size of the pizza base.
    
        Args:
            size (str): The size of the pizza base ("small", "medium", or "large").

        Raises:
            ValueError: If the size is not one of "small", "medium", or "large".
    '''
    def setSize(self, size):
        if size == "small":
            self.scaleCost(10) # Scale the cost based on the diameter
        elif size == "medium":
            self.scaleCost(12)
        elif size == "large":
            self.scaleCost(14)
        else:
            raise ValueError("Must be one of Small, Medium, Large")
        
    ''' Returns the size of the pizza base.

        Returns:
            str: The size of the pizza base ("small", "medium", or "large").
    '''
    def getSize(self):
        if self.__diameter == 10:
            return "small"
        if self.__diameter == 12:
            return "medium"
        if self.__diameter == 14:
            return "large"
    
    '''Returns a string representation of the pizza base.

        Returns:
            str: The string representation of the pizza base.
    '''
    def __str__(self):
        if self.__diameter is None:
            return f"{self.getName()}, diameter: Unknown, ${self.getPrice():.2f}"
        else:
            return f"{self.getSize()}, {self.getName()}, ${self.getPrice():.2f}"


'''Represents a pizza with a name, price, base, and toppings.
'''
class Pizza(Food):

    '''Initializes a new instance of the Pizza class.

        Args:
            name (str): The name of the pizza.
            price (float): The price of the pizza.
            base (PizzaBase): The original base of the pizza.
            toppings (list): A list of original toppings for the pizza.
    '''
    def __init__(self, name, price, base, toppings):
        super().__init__(name, price)
        self.originalBase = base.clone()
        self.currentBase = None
        self.originalToppings = []
        for t in toppings:
            self.originalToppings.append(t.clone())
        self.currentToppings = [t.clone() for t in toppings]

    '''Adds a topping to the pizza.

        Args:
            topping (Food): The topping to be added.
    '''
    def addTopping(self, topping):
        self.currentToppings.append(topping.clone())

    '''Removes a topping from the pizza.

        Args:
            topping (Food): The topping to be removed.
    '''
    def removeTopping(self, topping):
        self.currentToppings = [t for t in self.currentToppings if not t.equalCheck(topping)]

    '''Calculates and returns the total price of the pizza.

        Returns:
            float: The total price of the pizza.
    '''
    def getPrice(self):
        price = super().getPrice()
        # Calculate price difference for the base
        if self.currentBase is not None:
            price += self.currentBase.getPrice() - self.originalBase.getPrice()   

        # Calculate price difference for the toppings
        for topping in self.currentToppings:
            if not any(topping.equalCheck(originalTopping) for originalTopping in self.originalToppings):   # Check if the toppings in the currentTopping list is in the originalTopping list
                price += topping.getPrice()

        for topping in self.originalToppings:
            if not any(topping.equalCheck(currentTopping) for currentTopping in self.currentToppings):  # Check if the toppings in the originalTopping list is in the currentTopping list
                price -= topping.getPrice()

        return float(price)
    
    '''Creates and returns a clone of the pizza.

        Returns:
            Pizza: A clone of the pizza.
    '''
    def clone(self):
        if isinstance(self, Pizza):
            return type(self)(self.getName(), self.getPrice(), self.originalBase, self.originalToppings)
        else:
            raise TypeError('Cannot clone object of different class')

    '''Checks if the pizza is equal to another pizza.

        Args:
            other (Pizza): The other pizza to compare with.

        Returns:
            bool: True if the pizzas are equal, False otherwise.
    '''
    def equalCheck(self, other):
        if not isinstance(other, Pizza):
            return False
        if self.getName() != other.getName():
            return False
        if self.currentBase is not None and not self.currentBase.equalCheck(other.currentBase):
            return False
        if self.currentBase is None and not self.originalBase.equalCheck(other.originalBase):
            return False
        if len(self.currentToppings) != len(other.currentToppings):
            return False
        for i in range(len(self.currentToppings)):
            if not self.currentToppings[i].equalCheck(other.currentToppings[i]):
                return False
        return True

    '''Returns a string representation of the pizza.

        Returns:
            str: The string representation of the pizza.
    '''
    def __str__(self):
        toppings_str = (' ' * 4) + (', ').join(topping.getName() for topping in self.currentToppings)
        if self.currentBase is None:
            return f"Your Pizza: {self.getName()} {self.originalBase.getSize()} {self.originalBase.getName()} ${self.getPrice()}\n{toppings_str}"
        else:
            return f"Your Pizza: {self.getName()} {self.currentBase.getSize()} {self.currentBase.getName()} ${self.getPrice()}\n{toppings_str}"


'''Represents a pizza shop with ingredients, menu, and order history.
'''
class PizzaShop:
    
    '''Initializes a new instance of the PizzaShop class.
    '''
    def __init__(self):
        self.ingredients = []
        self.menu = []
        self.orderHistory = []

    '''Loads the ingredients from a file and adds them to the shop's ingredient list.
    '''
    def loadIngredients(self):
        with open(('files/ingredients.txt')) as file:
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


    '''Loads the menu from a file and adds the pizzas to the shop's menu.
    '''
    def loadMenu(self):
        with open(('files/menu.txt'), 'r') as file:
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
  

    '''Displays the menu and allows the user to order a pizza from the menu.

        Returns:
            Pizza: The selected pizza from the menu.
    '''
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

    '''Changes the size of a pizza based on user input.

        Args:
            pizza (Pizza): The pizza to change the size of.

        Returns:
            Pizza: The pizza with the updated size.
    '''
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

    '''Changes the base of a pizza based on user input.

        Args:
            pizza (Pizza): The pizza to change the base of.

        Returns:
            Pizza: The pizza with the updated base.
    '''
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

    '''Adds a topping to a pizza based on user input.

        Args:
            pizza (Pizza): The pizza to add the topping to.
    '''
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
    
    '''Removes a topping from a pizza based on user input.

        Args:
            pizza (Pizza): The pizza to remove the topping from.
    '''
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

    '''Displays the order history.
    '''
    def displayOrder(self):
        print("So far you have ordered...")
        for pizza in self.orderHistory:
            print(pizza)

    '''Saves the order receipt to a file.

        Args:
            customer_name (str): The name of the customer.
    '''
    def saveReceipt(self, customer_name):
        filename = (f"files/receipt/{customer_name}_receipt.txt")
        with open(filename, "w") as file:
            file.write("Receipt:\n")
            for pizza in self.orderHistory:
                file.write(str(pizza) + "\n")
            file.write(f"Enjoy your meal {customer_name}! :)")


    '''Displays the main menu interface and handles user interactions.
    '''
    def menuInterface(self):
        print("~~ Welcome to the Pizza Shop ~~")
        name = input("Please enter your name: ")
        while len(name.split()) < 1:
            name = input("Please enter at least 1 word for your name: ")
        exit_program = False
        while not exit_program:
            print("1. Order Pizza")
            print("2. Display orders")
            print("3. Exit")
            choice = input("How may I help you: ")

            if choice == '1':
                pizza_choice = self.orderPizza()
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
                        self.changeSize(pizza_choice)
                    elif sub_choice == '2':
                        # Code for changing pizza base
                        self.changeBase(pizza_choice)
                    elif sub_choice == '3':
                        # Code for adding topping
                        self.addTopping(pizza_choice)
                    elif sub_choice == '4':
                        # Code for removing topping
                        self.removeTopping(pizza_choice)
                    elif sub_choice == '5':
                        # Code for placing the order
                        self.orderHistory.append(pizza_choice)
                        sub_choice = '6'
                    elif sub_choice != '6':
                        print("Invalid submenu choice.")

            elif choice == '2':
                print("Displaying orders...")
                # Code to display orders
                self.displayOrder()

            elif choice == '3':
                self.saveReceipt(name)
                print(f"Have a good day, {name}! :)")
                exit_program = True

            else:
                print("Please select either 1, 2, or 3.")
# main function
def main():
    shop = PizzaShop()
    shop.loadIngredients()
    shop.loadMenu()
    shop.menuInterface()

    

#WARNING: Do not write any code in global scope

if __name__ == '__main__':
    main()