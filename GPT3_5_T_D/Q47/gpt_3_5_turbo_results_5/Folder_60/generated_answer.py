
import re

def palindromes_of_specific_lengths(string):
    substring = string[23:83].lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(32, 35):
            if i + j <= len(substring):
                sub = substring[i:i+j]
                if sub == sub[::-1] and re.match("^[a-zA-Z]+$", sub):
                    palindromes.add(sub)
    return palindromes
