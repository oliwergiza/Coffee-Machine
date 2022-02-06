class CoffeeMachine:
    def __init__(self, water_in_machine, milk_in_machine, beans_in_machine, cups_in_machine, money_in_machine):
        self.water_in_machine = water_in_machine
        self.milk_in_machine = milk_in_machine
        self.beans_in_machine = beans_in_machine
        self.cups_in_machine = cups_in_machine
        self.money_in_machine = money_in_machine

    def choose_action(self, action):
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.remaining()

    def is_available(self, type_of_coffee):
        if type_of_coffee == 1:
            can_make_water = self.water_in_machine // 250
            can_name_beans = self.beans_in_machine // 16
            if can_make_water > 0 and can_name_beans > 0:
                return True
            else:
                return False
        elif type_of_coffee == 2:
            can_make_water = self.water_in_machine // 350
            can_make_milk = self.milk_in_machine // 75
            can_name_beans = self.beans_in_machine // 20
            if can_make_water > 0 and can_make_milk > 0 and can_name_beans > 0:
                return True
            else:
                return False
        elif type_of_coffee == 3:
            can_make_water = self.water_in_machine // 200
            can_make_milk = self.milk_in_machine // 100
            can_name_beans = self.beans_in_machine // 12
            if can_make_water > 0 and can_make_milk > 0 and can_name_beans > 0:
                return True
            else:
                return False

    def not_enough(self, type_of_coffee):
        if type_of_coffee == 1:
            can_make_water = self.water_in_machine // 250
            can_name_beans = self.beans_in_machine // 16
            if can_make_water <= 0:
                print("Sorry, not enough water!")
            elif can_name_beans <= 0:
                print("Sorry, not enough coffee beans!")
        elif type_of_coffee == 2:
            can_make_water = self.water_in_machine // 350
            can_make_milk = self.milk_in_machine // 75
            can_name_beans = self.beans_in_machine // 20
            if can_make_water <= 0:
                print("Sorry, not enough water!")
            elif can_make_milk <= 0:
                print("Sorry, not enough milk!")
            elif can_name_beans <= 0:
                print("Sorry, not enough coffee beans!")
        elif type_of_coffee == 3:
            can_make_water = self.water_in_machine // 200
            can_make_milk = self.milk_in_machine // 100
            can_name_beans = self.beans_in_machine // 12
            if can_make_water <= 0:
                print("Sorry, not enough water!")
            elif can_make_milk <= 0:
                print("Sorry, not enough milk!")
            elif can_name_beans <= 0:
                print("Sorry, not enough coffee beans!")

    def buy(self):
        while True:
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            type_of_coffee = input()
            if type_of_coffee == "back":
                break
            else:
                if int(type_of_coffee) == 1 and self.is_available(1):
                    print("I have enough resources, making you a coffee!")
                    self.water_in_machine -= 250
                    self.beans_in_machine -= 16
                    self.cups_in_machine -= 1
                    self.money_in_machine += 4
                    break
                elif int(type_of_coffee) == 1 and not self.is_available(1):
                    self.not_enough(1)
                    break
                elif int(type_of_coffee) == 2 and self.is_available(2):
                    print("I have enough resources, making you a coffee!")
                    self.water_in_machine -= 350
                    self.milk_in_machine -= 75
                    self.beans_in_machine -= 20
                    self.cups_in_machine -= 1
                    self.money_in_machine += 7
                    break
                elif int(type_of_coffee) == 2 and not self.is_available(2):
                    self.not_enough(2)
                    break
                elif int(type_of_coffee) == 3 and self.is_available(3):
                    print("I have enough resources, making you a coffee!")
                    self.water_in_machine -= 200
                    self.milk_in_machine -= 100
                    self.beans_in_machine -= 12
                    self.cups_in_machine -= 1
                    self.money_in_machine += 6
                    break
                elif int(type_of_coffee) == 3 and not self.is_available(3):
                    self.not_enough(2)
                    break

    def fill(self):
        print("Write how many ml of water you want to add:")
        add_water = int(input())
        print("Write how many ml of milk you want to add:")
        add_milk = int(input())
        print("Write how many grams of coffee beans you want to add:")
        add_beans = int(input())
        print("Write how many disposable coffee cups you want to add:")
        add_cups = int(input())

        self.water_in_machine += add_water
        self.milk_in_machine += add_milk
        self.beans_in_machine += add_beans
        self.cups_in_machine += add_cups

    def take(self):
        print("I gave you", self.money_in_machine)
        self.money_in_machine = 0

    def remaining(self):
        print("The coffee machine has:")
        print('{} of water'.format(self.water_in_machine))
        print('{} of milk'.format(self.milk_in_machine))
        print('{} of beans'.format(self.beans_in_machine))
        print('{} of disposable cups'.format(self.cups_in_machine))
        print('${} of money'.format(self.money_in_machine))


def main():
    coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
    while True:
        print()
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        print()

        if action == "buy":
            coffee_machine.choose_action("buy")
        elif action == "fill":
            coffee_machine.choose_action("fill")
        elif action == "take":
            coffee_machine.choose_action("take")
        elif action == "remaining":
            coffee_machine.choose_action("remaining")
        elif action == "exit":
            break


if __name__ == '__main__':
    main()
