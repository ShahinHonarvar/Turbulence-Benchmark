
import re

def palindromes_of_specific_lengths(string):
    substring = string[11:98].lower()
    palindromes = set()
    for length in range(29, 63):
        for i in range(len(substring) - length):
            sub = substring[i:i+length]
            if sub == sub[::-1] and re.match('^[a-zA-Z]+$', sub):
                palindromes.add(sub)
    return palindromes
