
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^A-Za-z]', '', string.lower())
    palindromes = set()

    for i in range(len(string)-83):
        substring = string[i: i+84]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
