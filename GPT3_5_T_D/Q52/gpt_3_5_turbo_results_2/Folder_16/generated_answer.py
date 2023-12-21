
import re

def palindrome_of_length_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    palindromes = set()
    length = 255
    n = len(string)
    if n < length:
        return palindromes
    for i in range(n - length + 1):
        substring = string[i:i+length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
