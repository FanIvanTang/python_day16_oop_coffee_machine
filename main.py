from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def get_instrcution_from_user(coffee_menu):
    """
    get instruction from user and the valid input should be "espresso, latte, cappucccino, report, and off"
    and return the instruction
    """
    instructions = coffee_menu.get_items().split("/")
    
    instructions.append('off')
    instructions.append('report')
    


    user_input = input(f"What would you like? {coffee_menu.get_items()}: ")

    while user_input not in instructions:
        user_input = input(
            f"Opoos, wrong instruction, what would you like? ( {coffee_menu.get_items()})"
        )

    return user_input
    
def off_machine():
    """
    turn off machine
    """
    exit()


if __name__ == "__main__":
    
    thisMenu = Menu()
    
    coffeeMaker = CoffeeMaker()
    moneyMachine = MoneyMachine()

    
    
    while True:

        instruction = get_instrcution_from_user(coffee_menu=thisMenu)

        if instruction == "off":
            off_machine()

        elif instruction == "report":
            coffeeMaker.report()
            moneyMachine.report()
        else: 
            
            thisCoffee = thisMenu.find_drink(instruction)
            
            if coffeeMaker.is_resource_sufficient(thisCoffee):
                if moneyMachine.make_payment(thisCoffee.cost):
                    coffeeMaker.make_coffee(thisCoffee)
               
                
