
import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[1:10]
    for length in range(3, 8):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if re.match(r'^[a-zA-Z]+$', sub):
                if sub.lower() == sub.lower()[::-1]:
                    palindromes.add(sub)
    return palindromes
