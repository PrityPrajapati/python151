# 1. Print "Hello, World!"
print("Hello, World!")

# 2. Variables and Data Types
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Your name is {name} and your age is {age}.")

# 3. Arithmetic Operations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Modulus: {num1 % num2}")

# 4. Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

# 5. Swap Two Variables
var1 = input("Enter the first variable: ")
var2 = input("Enter the second variable: ")
print(f"Before swapping: var1 = {var1}, var2 = {var2}")
var1, var2 = var2, var1
print(f"After swapping: var1 = {var1}, var2 = {var2}")

# 6. Even or Odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 7. Check Vowel or Consonant
letter = input("Enter a single letter: ").lower()
if letter in 'aeiou':
    print("The letter is a vowel.")
elif letter.isalpha():
    print("The letter is a consonant.")
else:
    print("Invalid input. Please enter a single alphabetic character.")

# 8. Square, Cube, and Square Root
num = float(input("Enter a number: "))
print(f"Square: {num ** 2}")
print(f"Cube: {num ** 3}")
print(f"Square Root: {num ** 0.5}")

# 9. Area of Circle
radius = float(input("Enter the radius of the circle: "))
area = 3.14159 * radius ** 2
print(f"Area of the circle: {area}")

# 10. Simple Interest Calculation
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time in years: "))
simple_interest = (principal * rate * time) / 100
print(f"Simple Interest: {simple_interest}")
