
import re

def palindromes_of_specific_lengths(s):
    s = s[13:100].lower()
    palindromes = set()
    for l in range(26, 30):
        for i in range(len(s) - l + 1):
            substring = s[i:i + l]
            if substring == substring[::-1] and re.match('^[a-zA-Z]+$', substring):
                palindromes.add(substring)
    return palindromes
