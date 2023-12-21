
import re

def palindrome_of_length_n(string):
    string = re.sub(r'[^A-Za-z]', '', string.lower())
    palindromes = set()
    length = 23
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
