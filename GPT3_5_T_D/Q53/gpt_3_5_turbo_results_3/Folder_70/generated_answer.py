
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'\W', '', string.lower())
    palindromes = set()
    for i in range(len(string)):
        for j in range(len(string), i, -1):
            substr = string[i:j]
            if substr == substr[::-1] and len(substr) >= 11:
                palindromes.add(substr)
    return palindromes
