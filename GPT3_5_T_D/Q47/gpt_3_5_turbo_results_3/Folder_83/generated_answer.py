
import re

def palindromes_of_specific_lengths(s):
    s = s[75:96].lower()
    palindromes = set()
    for length in range(7, 10):
        for i in range(len(s) - length + 1):
            substring = s[i:i+length]
            if substring == substring[::-1] and re.match("^[a-zA-Z]+$", substring):
                palindromes.add(substring)
    return palindromes
