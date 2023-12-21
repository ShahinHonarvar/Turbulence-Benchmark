
import re

def palindromes_of_specific_lengths(string):
    substr = string[30:85].lower()
    palindromes = set()
    for length in range(12, 21):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub == sub[::-1] and re.match("^[a-zA-Z]+$", sub):
                palindromes.add(sub)
    return palindromes
