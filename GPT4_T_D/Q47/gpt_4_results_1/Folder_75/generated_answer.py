
import re

def palindromes_of_specific_lengths(s):
    s = s[31:75].lower()
    palindromes = set()
    for l in range(23, 40):
        for i in range(len(s)-l+1):
            substring = s[i:i+l]
            if substring == substring[::-1] and re.match('^[a-z]*$', substring):
                palindromes.add(substring)
    return palindromes
