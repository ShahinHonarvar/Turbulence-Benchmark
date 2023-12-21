
import re

def palindromes_of_specific_lengths(string):
    substring = string[36:93]
    substring = substring.lower()
    palindromes = set()
    for length in range(10, 36+1):
        for i in range(len(substring) - length + 1):
            substring_sub = substring[i:i+length]
            if substring_sub == substring_sub[::-1] and re.match("^[a-zA-Z]+$", substring_sub):
                palindromes.add(substring_sub)
    return palindromes
