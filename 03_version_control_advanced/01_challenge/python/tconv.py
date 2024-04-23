import time

def convert_celsius_to_fahrenheit():
    print("Enter the temperature in Celsius:")
    celsius = input()
    celsius = int(celsius)
    fahrenheit = (celsius * 9/5) + 32
    time.sleep(5)
    print(f"The Celsius temperature {celsius} you entered is {fahrenheit} in Fahrenheit.")

def convert_fahrenheit_to_celsius():
    print("Enter the temperature in Fahrenheit:")
    fahrenheit = input()
    fahrenheit = int(fahrenheit)
    celsius = 5 / 9 * (fahrenheit - 32)
    time.sleep(5)
    print(f"The Fahrenheit temperature {fahrenheit} you entered is {celsius} in Fahrenheit.")

def kelvin_to_fahrenheit():
    print("Enter the temperature in Kelvin:")
    kelvin = input()
    kelvin = int(kelvin)
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    time.sleep(5)
    print(f"The Kelvin temperature {kelvin} you entered is {fahrenheit} in Fahrenheit.")

def fahrenheit_to_kelvin():
    print("Enter the temperature in Fahrenheit:")
    fahrenheit = input()
    fahrenheit = int(fahrenheit)
    kelvin =  (fahrenheit - 32) * 5/9 + 273.15
    time.sleep(5)
    print(f"The Fahrenheit temperature {fahrenheit} you entered is {kelvin} in Kelvin.")

def kelvin_to_celsius():
    print("Enter the temperature in Kelvin:")
    kelvin = input()
    kelvin = int(kelvin)
    celsius = kelvin - 273.15
    time.sleep(5)
    print(f"The Kelvin temperature {kelvin} you entered is {celsius} in Celsius.")

def celsius_to_kelvin():
    print("Enter the temperature in Celsius:")
    celsius = input()
    celsius = int(celsius)
    kelvin = celsius + 273.15
    time.sleep(5)
    print(f"The Celsius temperature {celsius} you entered is {kelvin} in Kelvin.")

def main():
    print("Enter 1 if you want to convert from Fahrenheit to Celsius.")
    print("Enter 2 if you want to convert from Celsius to Fahrenheit")
    print("Enter 3 if you want to convert from Kelvin to Fahrenheit")
    print("Enter 4 if you want to convert from Fahrenheit to Kelvin")
    print("Enter 5 if you want to convert from Kelvin to Celsius")
    print("Enter 6 if you want to convert from Celsius to Kelvin")

    is_valid = False

    while not is_valid:
        user_input = input()

        if user_input == '1':
            convert_celsius_to_fahrenheit()
            is_valid = True
        elif user_input == '2':
            convert_fahrenheit_to_celsius()
            is_valid = True
        elif user_input == '3':
            kelvin_to_fahrenheit()
            is_valid = True
        elif user_input == '4':
            fahrenheit_to_kelvin()
            is_valid = True
        elif user_input == '5':
            kelvin_to_celsius()
            is_valid = True
        elif user_input == '6':
            celsius_to_kelvin()
            is_valid = True
        else:
            print("Incorrect input. Please try again later")


main()