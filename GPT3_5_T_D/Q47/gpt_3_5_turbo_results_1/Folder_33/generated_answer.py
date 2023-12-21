
import re

def palindromes_of_specific_lengths(s):
    s = s[130:296].lower()
    palindromes = set()
    for length in range(103, 159):
        for i in range(len(s) - length + 1):
            substring = s[i:i+length]
            if substring == substring[::-1] and re.match('^[a-zA-Z]+$', substring):
                palindromes.add(substring)
    return palindromes
