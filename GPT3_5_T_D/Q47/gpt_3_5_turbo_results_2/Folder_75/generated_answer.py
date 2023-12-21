
import re

def palindromes_of_specific_lengths(string):
    substring = string[31:75].lower()
    palindromes = set()

    for length in range(23, 40):
        for i in range(len(substring) - length + 1):
            substring_ = substring[i:i+length]
            if re.match('^[a-zA-Z]+$', substring_):
                if substring_ == substring_[::-1]:
                    palindromes.add(substring_)

    return palindromes
