
import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+29, len(s)+1):
            substring = s[i:j]
            if re.match('^[a-zA-Z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
