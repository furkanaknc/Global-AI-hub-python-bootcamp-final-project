import csv
from datetime import datetime

class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

class Decorator(Pizza):
    def __init__(self, component, description, cost):
        super().__init__(description, cost)
        self.component = component

    def get_description(self):
        return self.component.get_description() + ' ' + super().get_description()

    def get_cost(self):
        return self.component.get_cost() + super().get_cost()

class Olives(Decorator):
    def __init__(self, component):
        super().__init__(component, "Olives", 2.0)

class Mushrooms(Decorator):
    def __init__(self, component):
        super().__init__(component, "Mushrooms", 1.5)

class GoatCheese(Decorator):
    def __init__(self, component):
        super().__init__(component, "Goat Cheese", 3.0)

class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component, "Meat", 2.5)

class Onions(Decorator):
    def __init__(self, component):
        super().__init__(component, "Onions", 1.0)

class Corn(Decorator):
    def __init__(self, component):
        super().__init__(component, "Corn", 1.0)

def add_order_to_database(order):
    with open("Orders_Database.csv", mode='a', newline='') as database_file:
        fieldnames = ['order_number', 'customer_name', 'pizza_description', 'toppings', 'cost','id_number','card_number','card_password','order_time']
        writer = csv.DictWriter(database_file, fieldnames=fieldnames)

        if database_file.tell() == 0:
            writer.writeheader()

        writer.writerow({
            'order_number': order['order_number'],
            'customer_name': order['customer_name'],
            'pizza_description': order['pizza_description'],
            'toppings': ', '.join(order['toppings']),
            'cost': order['cost'],
            'id_number':order['id_number'],
            'card_number':order['card_number'],
            'card_password':order['card_password'],
            'order_time': order['order_time'].strftime('%Y-%m-%d %H:%M:%S')
        })

def main():
    pizza_options = {
        "Classic Pizza": 10.0,
        "Margherita Pizza": 12.0,
        "Turk Pizza": 15.0,
        "Dominos Pizza": 18.0
    }

    order_database = "Orders_Database.csv"

    while True:
           

        # Print the available pizza options
        print("Please select a pizza:")
        with open('Menu.txt', 'r') as f:
            pizza_list = f.readlines()

            pizza_list = [option.strip() for option in pizza_list]

            pizza_bases = pizza_list[1:5]
            sauces = pizza_list[6:12]
        for option in pizza_bases:
            num1, p_name = option.split(":")
            print(num1.strip() + " " + p_name.strip())
        # Prompt the user to enter their pizza choice
        pizza_choice = input("Enter the number of the pizza you want: ")
        
        # Create the base pizza
        if pizza_choice =="1":
            pizza = Pizza("Classic Pizza", pizza_options["Classic Pizza"])
        elif pizza_choice =="2":
            pizza = Pizza("Margherita Pizza", pizza_options["Margherita Pizza"])
        elif pizza_choice =="3":
            pizza = Pizza("Turk Pizza", pizza_options["Turk Pizza"])
        elif pizza_choice =="4":
            pizza = Pizza("Dominos Pizza", pizza_options["Dominos Pizza"])   

        # Ask the user if they want to add toppings
        toppings = []
        while True:
            add_topping = input("Do you want to add a topping? (y/n): ")
            if add_topping.lower() == "y":
                print("Please select a topping:")
                for option in sauces:
                    num2, s_name = option.split(":")
                    print(num2.strip() + " " + s_name.strip())

                topping_choice = input("Enter the number of the topping you want: ")
                if topping_choice == "11":
                    pizza = Olives(pizza)
                    toppings.append("Olives")
                elif topping_choice == "12":
                    pizza = Mushrooms(pizza)
                    toppings.append("Mushrooms")
                elif topping_choice == "13":
                    pizza = GoatCheese(pizza)
                    toppings.append("Goat Cheese")
                elif topping_choice == "14":
                    pizza = Meat(pizza)
                    toppings.append("Meat")
                elif topping_choice == "15":
                    pizza = Onions(pizza)
                    toppings.append("Onions")
                elif topping_choice == "16":
                    pizza = Corn(pizza)
                    toppings.append("Corn")
                else:
                    print("Invalid topping choice")
            elif add_topping.lower() == "n":
                break
            else:
                print("Invalid input")

        # Calculate the total cost of the pizza
        total_cost = pizza.get_cost()

        # Get user information and process payment
        customer_name = input("Please enter your name: ")
        id_number = input("Please enter your ID number: ")
        card_number = input("Please enter your credit card number: ")
        card_password = input("Please enter your credit card password: ")

        # Display the order details to the user
        print("Thank you for your order!")
        print(f"Customer name: {customer_name}")
        print(f"Pizza description: {pizza.get_description()}")
        print(f"Toppings: {', '.join(toppings)}")
        print(f"Cost: ${total_cost:.2f}")

        # Add the order to the database
        order_number = datetime.now().strftime("%Y%m%d%H%M%S")
        order_time = datetime.now()
        order = {
            "order_number": order_number,
            "customer_name": customer_name,
            "pizza_description": pizza.get_description(),
            "toppings": toppings,
            "cost": total_cost,
            "id_number": id_number,
            "card_number": card_number,
            "card_password":card_password,
            "order_time": order_time
        }
        add_order_to_database(order)

        another_order = input("Do you want to place another order? (y/n)").lower()
        if another_order == "y":
            continue
        else:
            break



if __name__ == '__main__':
    main()
