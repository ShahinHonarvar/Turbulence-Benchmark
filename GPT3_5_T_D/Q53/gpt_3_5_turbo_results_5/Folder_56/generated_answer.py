
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^A-Za-z]', '', string)
    string = string.lower()
    palindromes = set()
    length = len(string)
    for i in range(length):
        for j in range(i + 84, length + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
