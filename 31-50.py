# 31. List Operations
lst = [1, 2, 3]
print(f"Initial list: {lst}")

# Append
lst.append(4)
print(f"After append(4): {lst}")

# Insert
lst.insert(1, 10)
print(f"After insert(1, 10): {lst}")

# Remove
lst.remove(2)
print(f"After remove(2): {lst}")

# Pop
popped = lst.pop()
print(f"After pop(): {lst}, popped element: {popped}")

# 32. Maximum and Minimum in a List
lst = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print(f"Maximum: {max(lst)}, Minimum: {min(lst)}")

# 33. Second Largest Element
lst = [int(x) for x in input("Enter unique integers separated by spaces: ").split()]
lst.sort()
print(f"Second largest element: {lst[-2]}")

# 34. Sum and Average of a List
lst = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print(f"Sum: {sum(lst)}, Average: {sum(lst) / len(lst)}")

# 35. Count Positive, Negative, Zero
lst = [int(x) for x in input("Enter integers separated by spaces: ").split()]
positive = sum(1 for x in lst if x > 0)
negative = sum(1 for x in lst if x < 0)
zero = sum(1 for x in lst if x == 0)
print(f"Positive: {positive}, Negative: {negative}, Zero: {zero}")

# 36. Remove Duplicates from a List
lst = [int(x) for x in input("Enter integers separated by spaces: ").split()]
unique_lst = list(set(lst))
print(f"List without duplicates: {unique_lst}")

# 37. Concatenate Two Lists
lst1 = [int(x) for x in input("Enter the first list: ").split()]
lst2 = [int(x) for x in input("Enter the second list: ").split()]
print(f"Concatenated list: {lst1 + lst2}")

# 38. List Reversal
def reverse_list(lst):
    return lst[::-1]

lst = [int(x) for x in input("Enter a list: ").split()]
print(f"Reversed list: {reverse_list(lst)}")

# 39. Find Common Elements of Two Lists
lst1 = [int(x) for x in input("Enter the first list: ").split()]
lst2 = [int(x) for x in input("Enter the second list: ").split()]
common = list(set(lst1) & set(lst2))
print(f"Common elements: {common}")

# 40. Element-wise Sum of Two Lists
lst1 = [int(x) for x in input("Enter the first list: ").split()]
lst2 = [int(x) for x in input("Enter the second list: ").split()]
sum_lst = [x + y for x, y in zip(lst1, lst2)]
print(f"Element-wise sum: {sum_lst}")

# 41. Tuple Creation and Access
tup = ("apple", "banana", "cherry", "date")
index = int(input(f"Enter an index (0 to {len(tup) - 1}): "))
if 0 <= index < len(tup):
    print(f"Element at index {index}: {tup[index]}")
else:
    print("Invalid index")

# 42. Tuple to List
tup = tuple(input("Enter elements separated by spaces: ").split())
lst = list(tup)
lst.append("new_element")
tup = tuple(lst)
print(f"Modified tuple: {tup}")

# 43. Check if Element Exists in Tuple
tup = ("apple", "banana", "cherry")
element = input("Enter an element to check: ")
print(f"Exists in tuple: {element in tup}")

# 44. Dictionary: Word Count
text = input("Enter a string: ")
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print(f"Word count: {word_count}")

# 45. Dictionary: Student Grades
grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
name = input("Enter the student's name: ")
print(f"Grade: {grades.get(name, 'Student not found')}")

# 46. Dictionary: Keys and Values
d = {"name": "Alice", "age": 25, "city": "New York"}
print(f"Keys: {list(d.keys())}")
print(f"Values: {list(d.values())}")

# 47. Merge Two Dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged_dict = {**d1, **d2}
print(f"Merged dictionary: {merged_dict}")

# 48. Invert Dictionary
d = {"a": 1, "b": 2, "c": 3}
if len(set(d.values())) == len(d.values()):
    inverted = {v: k for k, v in d.items()}
    print(f"Inverted dictionary: {inverted}")
else:
    print("Cannot invert: duplicate values found")

# 49. Set Operations
lst1 = [int(x) for x in input("Enter the first list: ").split()]
lst2 = [int(x) for x in input("Enter the second list: ").split()]
set1, set2 = set(lst1), set(lst2)
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference (set1 - set2): {set1 - set2}")

# 50. Set Membership Testing
names = {"Alice", "Bob", "Charlie"}
name = input("Enter a name to check: ")
print(f"Exists in set: {name in names}")
