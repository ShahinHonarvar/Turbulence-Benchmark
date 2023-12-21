
import re

def palindrome_of_length_at_least_n(s):
    s_lower = s.lower()
    palindromes = set()
    for i in range(len(s_lower) - 96):
        for j in range(i + 96, len(s_lower)):
            if s_lower[i:j+1] == s_lower[i:j+1][::-1] and re.match('^[a-zA-Z]+$', s_lower[i:j+1]):
                palindromes.add(s_lower[i:j+1])
    return palindromes
