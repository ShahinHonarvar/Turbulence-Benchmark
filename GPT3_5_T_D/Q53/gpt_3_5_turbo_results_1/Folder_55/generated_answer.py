
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+1, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and len(substring) >= 83:
                palindromes.add(substring)
    return palindromes
