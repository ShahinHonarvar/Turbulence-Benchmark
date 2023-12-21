
import re

def palindrome_of_length_n(s):
    palindromes = set()
    l = 47
    s = s.lower()
    for i in range(len(s) - l + 1):
        substring = s[i:i+l]
        if re.match('^[a-zA-Z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
