
import re

def palindromes_of_specific_lengths(s):
    s = s[11:97].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 45, min(i + 53, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and re.match('^[a-z]*$', substring):
                palindromes.add(substring)
    return palindromes
