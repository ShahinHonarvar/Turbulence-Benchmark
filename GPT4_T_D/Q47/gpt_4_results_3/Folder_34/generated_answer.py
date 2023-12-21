
import re

def palindromes_of_specific_lengths(s):
    s = s[200:301].lower()
    palindromes = set()
    for length in range(10, 51):
        for start in range(0, len(s) - length + 1):
            sub = s[start:start+length]
            if sub == sub[::-1] and re.match("^[a-z]*$", sub):
                palindromes.add(sub)
    return palindromes
