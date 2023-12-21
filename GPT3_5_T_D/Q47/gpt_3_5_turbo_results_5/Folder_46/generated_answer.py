
import re

def palindromes_of_specific_lengths(string):
    substring = string[11:98]
    palindromes = set()

    for length in range(29, 63):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if re.match('^[A-Za-z]+$', sub):
                if sub.lower() == sub[::-1].lower():
                    palindromes.add(sub)

    return palindromes
