# 21. Create a Simple Calculator (Functions)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Division by zero is not allowed"

# User interaction
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()

if operation == "add":
    print(f"Result: {add(num1, num2)}")
elif operation == "subtract":
    print(f"Result: {subtract(num1, num2)}")
elif operation == "multiply":
    print(f"Result: {multiply(num1, num2)}")
elif operation == "divide":
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid operation")

# 22. Power Function
def power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    return result if exponent >= 0 else 1 / result

print(power(2, 3))  # Example: 2^3 = 8

# 23. Count Characters in a String (Function)
def count_characters(string):
    return len(string)

string = input("Enter a string: ")
print(f"Number of characters: {count_characters(string)}")

# 24. Check Prime (Function)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
print(f"{number} is prime: {is_prime(number)}")

# 25. Fibonacci Series (Function)
def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(f"Fibonacci series: {fibonacci(n)}")

# 26. GCD of Two Numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(24, 36))  # Example: GCD of 24 and 36 is 12

# 27. LCM of Two Numbers
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

print(lcm(24, 36))  # Example: LCM of 24 and 36 is 72

# 28. Factorial (Recursive)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Example: 5! = 120

# 29. Tower of Hanoi
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

tower_of_hanoi(3, 'A', 'C', 'B')  # Example: 3 disks from A to C using B

# 30. Count Occurrences of an Element
def count_occurrences(lst, x):
    return lst.count(x)

lst = [1, 2, 3, 4, 2, 2, 5]
x = 2
print(f"{x} occurs {count_occurrences(lst, x)} times in the list.")
