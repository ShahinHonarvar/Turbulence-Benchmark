
import re

def palindromes_of_specific_lengths(string):
    string = string.lower()
    substring = string[75:96]
    palindromes = set()

    for length in range(7, 10):
        for i in range(len(substring) - length + 1):
            sub = substring[i : i + length]
            if sub == sub[::-1] and re.match("^[a-zA-Z]+$", sub):
                palindromes.add(sub)
    
    return palindromes
