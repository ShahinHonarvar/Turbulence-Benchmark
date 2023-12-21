
import re

def palindromes_of_specific_lengths(string):
    substring = string[23:95]
    palindromes = set()

    for i in range(17, 56):
        for j in range(len(substring) - i + 1):
            sub = substring[j: j + i]
            sub_upper = sub.upper()

            if sub == sub[::-1] and re.match("^[A-Z]+$", sub_upper):
                palindromes.add(sub)

    return palindromes
