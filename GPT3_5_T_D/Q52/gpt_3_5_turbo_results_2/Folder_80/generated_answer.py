
import re

def palindrome_of_length_n(string):
    palindromes = set()

    for i in range(len(string)-275):
        substring = string[i:i+276].lower()
        if re.match('^[a-zA-Z]+$', substring) and substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
