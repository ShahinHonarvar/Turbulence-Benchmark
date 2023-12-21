
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub(r'\W', '', s).lower()
    n = 36
    palindromes = set()
    for i in range(n, len(s) + 1):
        for j in range(len(s) - i + 1):
            sub = s[j:j+i]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes
