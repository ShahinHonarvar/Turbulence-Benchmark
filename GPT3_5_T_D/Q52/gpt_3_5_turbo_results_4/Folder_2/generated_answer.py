
import re

def palindrome_of_length_n(string):
    result = set()
    string = re.sub(r'[^A-Za-z]', '', string.lower())
    length = 147
    for i in range(len(string) - length + 1):
        substring = string[i: i + length]
        if substring == substring[::-1]:
            result.add(substring)
    return result
