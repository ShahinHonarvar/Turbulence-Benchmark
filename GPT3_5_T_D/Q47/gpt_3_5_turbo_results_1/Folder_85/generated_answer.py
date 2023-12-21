
import re

def palindromes_of_specific_lengths(s):
    s = s.lower()
    indices_range = range(29, 99)
    palindromes = set()

    for i in indices_range:
        for length in range(6, 10):
            substring = s[i:i+length]
            if re.match('^[a-zA-Z]+$', substring):
                if substring == substring[::-1]:
                    palindromes.add(substring)

    return palindromes
