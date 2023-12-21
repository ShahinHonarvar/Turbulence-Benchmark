
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    lower_string = string.lower()
    length = len(lower_string)
    palindromes = set()
    
    if length >= 64:
        for i in range(length - 63):
            substring = lower_string[i:i+64]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
