
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)-8):
        for j in range(i+8, len(string)):
            substring = string[i:j+1]
            if re.match(r'^[a-zA-Z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
