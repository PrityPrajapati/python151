# 61. Armstrong Number
def is_armstrong(number):
    digits = [int(d) for d in str(number)]
    return sum(d ** len(digits) for d in digits) == number

number = int(input("Enter a number: "))
print(f"{number} is an Armstrong number: {is_armstrong(number)}")

# 62. Strong Number
import math

def is_strong_number(number):
    digits = [int(d) for d in str(number)]
    return sum(math.factorial(d) for d in digits) == number

number = int(input("Enter a number: "))
print(f"{number} is a Strong number: {is_strong_number(number)}")

# 63. Perfect Number
def is_perfect_number(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

number = int(input("Enter a number: "))
print(f"{number} is a Perfect number: {is_perfect_number(number)}")

# 64. Sum of Digits
number = int(input("Enter a number: "))
sum_of_digits = sum(int(d) for d in str(number))
print(f"Sum of digits: {sum_of_digits}")

# 65. Binary to Decimal Conversion
binary = input("Enter a binary number: ")
decimal = int(binary, 2)
print(f"Decimal equivalent: {decimal}")

# 66. Decimal to Binary Conversion
decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)[2:]
print(f"Binary equivalent: {binary}")

# 67. Prime Factors of a Number
def prime_factors(number):
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    return factors

number = int(input("Enter a number: "))
print(f"Prime factors: {prime_factors(number)}")

# 68. Number to Words
def number_to_words(number):
    words_map = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }
    return ' '.join(words_map[int(d)] for d in str(number))

number = int(input("Enter a number: "))
print(f"Number in words: {number_to_words(number)}")

# 69. LCM of a Range
from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_of_range(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

n = int(input("Enter the range (1 to n): "))
print(f"LCM of numbers from 1 to {n}: {lcm_of_range(n)}")

# 70. Sieve of Eratosthenes
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]

n = int(input("Enter the limit: "))
print(f"Prime numbers up to {n}: {sieve_of_eratosthenes(n)}")
