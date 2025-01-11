# 11. Largest of Three Numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
largest = max(num1, num2, num3)
print(f"The largest number is: {largest}")

# 12. Leap Year Checker
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 13. Multiplication Table
number = int(input("Enter a positive integer: "))
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 14. Sum of N Natural Numbers
n = int(input("Enter a positive integer: "))
sum_n = n * (n + 1) // 2
print(f"Sum of the first {n} natural numbers is: {sum_n}")

# 15. Factorial of a Number
num = int(input("Enter a non-negative integer: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is: {factorial}")

# 16. Number Guessing (While Loop)
import random
target = random.randint(1, 100)
guess = None
print("Guess the number between 1 and 100.")
while guess != target:
    guess = int(input("Your guess: "))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")

# 17. Count Digits of a Number
number = int(input("Enter a positive integer: "))
digits = len(str(number))
print(f"The number of digits in {number} is: {digits}")

# 18. Reverse a Number (While Loop)
number = int(input("Enter a positive integer: "))
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
print(f"The reversed number is: {reversed_number}")

# 19. Sum of Even and Odd Numbers Separately
n = int(input("Enter a positive integer: "))
sum_even = sum_odd = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"Sum of even numbers: {sum_even}")
print(f"Sum of odd numbers: {sum_odd}")

# 20. Palindrome Checker (Integer)
number = int(input("Enter a positive integer: "))
original = number
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
if original == reversed_number:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")
