# *************************************************************
# Lab Exercise 1: Temperature Converter                       *
# Programmed By: MARGARETTE VERGARA                           *
# Date Submitted: September 27, 2024                          *
# *************************************************************

def main():
    temperature = float(input('Enter the temperature: '))
    conversion = input('Convert from Celsius to Fahrenheit (C) or Fahrenheit to Celsius (F): ')
    if conversion == 'C':
        result = (temperature * 9/5) + 32
        print(f'{temperature} degrees Celsius is equal to {result} degrees Fahrenheit.')
    elif conversion == 'F':
        result = (temperature - 32) * 5/9
        print(f'{temperature} degrees Fahrenheit is equal to {result} degrees Celsius.')
    else:
        print("Invalid input. Please enter 'C' or 'F' for the conversion.")


if __name__ == '__main__':
    main()
