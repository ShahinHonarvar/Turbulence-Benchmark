
import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = 63

    for i in range(len(s) - n + 1):
        sub = s[i:i+n]
        if sub == sub[::-1] and re.match('^[a-zA-Z]+$', sub):
            palindromes.add(sub.lower())

    return palindromes
