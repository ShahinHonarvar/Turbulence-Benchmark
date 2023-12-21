
import re

def palindromes_of_specific_lengths(string):
    substring = string[16:78]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(43, 48):
            if i+j <= len(substring):
                sub = substring[i:i+j]
                if sub.lower() == sub.lower()[::-1] and re.match("^[a-zA-Z]+$", sub):
                    palindromes.add(sub)
    return palindromes
