
import re

def palindrome_of_length_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    palindromes = set()
    for i in range(len(string)-256):
        substring = string[i:i+257]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
