
import re

def palindromes_of_specific_lengths(string):
    substring = string[10:60].lower()
    palindromes = set()

    for length in range(18, 37):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub == sub[::-1] and re.match("^[a-zA-Z]+$", sub):
                palindromes.add(sub)

    return palindromes
