
import re

def palindromes_of_specific_lengths(s):
    s = s[26:85].lower()
    palindromes = set()
    for length in range(30, 47):
        for i in range(0, len(s) - length + 1):
            substring = s[i:i+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
