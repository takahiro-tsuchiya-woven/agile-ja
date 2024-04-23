def convert_celsius_to_fahrenheit():
    print("Enter the temperature in Celsius:")
    celsius = input()
    celsius = int(celsius)
    fahrenheit = (celsius * 9/5) + 32
    print(f"The Celsius temperature {celsius} you entered is {fahrenheit} in Fahrenheit.")

def convert_fahrenheit_to_celsius():
    print("Enter the temperature in Fahrenheit:")
    fahrenheit = input()
    fahrenheit = int(fahrenheit)
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"The Fahrenheit temperature {fahrenheit} you entered is {celsius} in Fahrenheit.")

def kelvin_to_fahrenheit():
    print("Enter the temperature in Kelvin:")
    kelvin = input()
    kelvin = int(kelvin)
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    print(f"The Kelvin temperature {kelvin} you entered is {fahrenheit} in Fahrenheit.")

def fahrenheit_to_kelvin():
    print("Enter the temperature in Fahrenheit:")
    fahrenheit = input()
    fahrenheit = int(fahrenheit)
    kelvin =  (fahrenheit - 32) * 5/9 + 273.15
    print(f"The Fahrenheit temperature {fahrenheit} you entered is {kelvin} in Kelvin.")

def kelvin_to_celsius():
    print("Enter the temperature in Kelvin:")
    kelvin = input()
    kelvin = int(kelvin)
    celsius = kelvin - 273.15
    print(f"The Kelvin temperature {kelvin} you entered is {celsius} in Celsius.")

def celsius_to_kelvin():
    print("Enter the temperature in Celsius:")
    celsius = input()
    celsius = int(celsius)
    kelvin = celsius + 273.15
    print(f"The Celsius temperature {celsius} you entered is {kelvin} in Kelvin.")

def main():
    print("Enter c if you want to convert from Fahrenheit to Celsius.")
    print("Enter f if you want to convert from Celsius to Fahrenheit")

    user_input = input()

    if user_input == 'c':
        convert_celsius_to_fahrenheit
    elif user_input == 'f':
        convert_fahrenheit_to_celsius
    else:
        print("Incorrect input. Please try again later")


main()