
import re

def palindromes_of_specific_lengths(string):
    substring = string[17:96]
    palindromes = set()
    for length in range(13, 50):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub.lower() == sub[::-1].lower() and re.match("^[a-zA-Z]+$", sub):
                palindromes.add(sub)
    return palindromes
