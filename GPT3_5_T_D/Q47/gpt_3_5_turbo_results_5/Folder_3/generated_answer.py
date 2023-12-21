
import re

def palindromes_of_specific_lengths(s):
    substring = s[27:96].lower()
    palindromes = set()
    for i in range(len(substring) - 51 + 1):
        for j in range(49, 51 + 1):
            if substring[i:i+j] == substring[i:i+j][::-1] and re.match('^[a-zA-Z]+$', substring[i:i+j]):
                palindromes.add(substring[i:i+j])
    return palindromes
