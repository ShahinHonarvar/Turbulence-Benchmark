
import re

def palindrome_of_length_n(string):
    string = string.lower()
    string = re.sub(r'[^a-z]', '', string)
    palindromes = set()
    for i in range(len(string) - 40):
        substring = string[i:i + 41]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
