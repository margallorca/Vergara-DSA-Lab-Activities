# *************************************************************
# Lab Exercise 2: Ohm's Law Calculator                        *
# Programmed By: MARGARETTE VERGARA                           *
# Date Submitted: September 27, 2024                          *
# *************************************************************

def ohms_law_calculator():
    print("Ohm's Law Calculator")
    print("What would you like to calculate?")
    print("1. Voltage")
    print("2. Current")
    print("3. Resistance")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        current = float(input("Enter the current in Amperes: "))
        resistance = float(input("Enter the resistance in Ohms: "))
        try:
            voltage = current * resistance
            print(f"The voltage is {voltage} Volts")
        except ZeroDivisionError:
            print("Error: Division by zero")
    elif choice == 2:
        voltage = float(input("Enter the voltage in Volts: "))
        resistance = float(input("Enter the resistance in Ohms: "))
        try:
            current = voltage / resistance
            print(f"The current is {current} Amperes")
        except ZeroDivisionError:
            print("Error: Division by zero")
    elif choice == 3:
        voltage = float(input("Enter the voltage in Volts: "))
        current = float(input("Enter the current in Amperes: "))
        try:
            resistance = voltage / current
            print(f"The resistance is {resistance} Ohms")
        except ZeroDivisionError:
            print("Error: Division by zero")
    else:
        print("Invalid choice")


ohms_law_calculator()
