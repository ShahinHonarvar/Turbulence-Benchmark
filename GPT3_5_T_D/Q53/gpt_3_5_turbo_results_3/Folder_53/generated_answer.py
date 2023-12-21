
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)-63):
        if re.match(r'[a-z]+$', string[i:i+64]):
            if string[i:i+64] == string[i:i+64][::-1]:
                palindromes.add(string[i:i+64])
    return palindromes
