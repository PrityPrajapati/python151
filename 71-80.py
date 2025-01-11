# 71. Write to File
text = input("Enter text to write to file: ")
with open("output.txt", "w") as file:
    file.write(text)
print("Text written to 'output.txt'.")

# 72. Read from File
try:
    with open("output.txt", "r") as file:
        content = file.read()
    print("File content:\n", content)
except FileNotFoundError:
    print("File 'output.txt' not found.")

# 73. Copy File
source = input("Enter source file name: ")
destination = input("Enter destination file name: ")
try:
    with open(source, "r") as src, open(destination, "w") as dest:
        dest.write(src.read())
    print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found.")

# 74. Count Lines in a File
filename = input("Enter file name: ")
try:
    with open(filename, "r") as file:
        lines = file.readlines()
    print(f"Total lines: {len(lines)}")
except FileNotFoundError:
    print("File not found.")

# 75. Count Words in a File
filename = input("Enter file name: ")
try:
    with open(filename, "r") as file:
        words = file.read().split()
    print(f"Total words: {len(words)}")
except FileNotFoundError:
    print("File not found.")

# 76. Find Longest Line in a File
filename = input("Enter file name: ")
try:
    with open(filename, "r") as file:
        longest_line = max(file, key=len)
    print("Longest line:", longest_line.strip())
except FileNotFoundError:
    print("File not found.")

# 77. Search for a Word in a File
filename = input("Enter file name: ")
word = input("Enter word to search: ")
try:
    with open(filename, "r") as file:
        lines = file.readlines()
    for i, line in enumerate(lines, start=1):
        if word in line:
            print(f"Word found on line {i}: {line.strip()}")
except FileNotFoundError:
    print("File not found.")

# 78. Append to a File
text = input("Enter text to append to file: ")
with open("output.txt", "a") as file:
    file.write(text + "\n")
print("Text appended to 'output.txt'.")

# 79. Remove Blank Lines
input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")
try:
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            if line.strip():
                outfile.write(line)
    print(f"Blank lines removed and content saved to '{output_file}'.")
except FileNotFoundError:
    print("File not found.")

# 80. File Statistics
filename = input("Enter file name: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        lines = content.splitlines()
        words = content.split()
    print(f"Total characters: {len(content)}")
    print(f"Total lines: {len(lines)}")
    print(f"Total words: {len(words)}")
except FileNotFoundError:
    print("File not found.")
