# 51. Reverse a String
string = input("Enter a string: ")
print(f"Reversed string: {string[::-1]}")

# 52. Palindrome String Checker
string = input("Enter a string: ")
is_palindrome = string == string[::-1]
print(f"'{string}' is a palindrome: {is_palindrome}")

# 53. Count Vowels in a String
def count_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)

string = input("Enter a string: ")
print(f"Number of vowels: {count_vowels(string)}")

# 54. Check Anagram
def are_anagrams(str1, str2):
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(f"'{str1}' and '{str2}' are anagrams: {are_anagrams(str1, str2)}")

# 55. Remove Spaces
string = input("Enter a string: ")
print(f"String without spaces: {string.replace(' ', '')}")

# 56. Longest Word in a Sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print(f"The longest word is: '{longest_word}' with length {len(longest_word)}")

# 57. String Case Conversion
string = input("Enter a string: ")
print(f"Uppercase: {string.upper()}")
print(f"Lowercase: {string.lower()}")
print(f"Title Case: {string.title()}")

# 58. Capitalize Every Word
string = input("Enter a string: ")
capitalized = ' '.join(word.capitalize() for word in string.split())
print(f"String with capitalized words: {capitalized}")

# 59. Count Special Characters
import string as str_lib

def count_special_characters(string):
    special_chars = str_lib.punctuation
    return sum(1 for char in string if char in special_chars)

string = input("Enter a string: ")
print(f"Number of special characters: {count_special_characters(string)}")

# 60. Character Frequency in String
def char_frequency(string):
    freq = {}
    for char in string:
        freq[char] = freq.get(char, 0) + 1
    return freq

string = input("Enter a string: ")
print(f"Character frequency: {char_frequency(string)}")
