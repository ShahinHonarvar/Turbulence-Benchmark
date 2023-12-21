
import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = re.sub(r'[^A-Za-z]', '', s.lower())

    for i in range(len(s) - 68):
        for j in range(i + 69, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    
    return palindromes
