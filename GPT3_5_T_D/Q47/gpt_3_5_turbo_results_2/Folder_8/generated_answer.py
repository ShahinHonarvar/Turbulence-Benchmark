
import re

def palindromes_of_specific_lengths(string):
    substring = string[17:73].lower()
    palindromes = set()
    for i in range(len(substring) - 51):
        for j in range(i + 50, len(substring) + 1):
            sub = substring[i:j]
            if sub == sub[::-1] and re.match("^[a-zA-Z]+$", sub):
                palindromes.add(sub.lower())
    return palindromes
