
import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)-14):
        substring = s[i:i+15]
        if substring == substring[::-1] and re.match("^[a-zA-Z]+$", substring):
            palindromes.add(substring)
    return palindromes
