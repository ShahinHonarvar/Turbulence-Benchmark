
import re

def palindromes_of_specific_lengths(string):
    substring = string[15:87]
    palindromes = set()
    for i in range(len(substring) - 50):
        for j in range(i + 51, len(substring) + 1):
            sub = substring[i:j]
            sub_lower = sub.lower()
            if sub_lower == sub_lower[::-1] and re.match(r'^[a-zA-Z]+$', sub):
                palindromes.add(sub)
    return palindromes
