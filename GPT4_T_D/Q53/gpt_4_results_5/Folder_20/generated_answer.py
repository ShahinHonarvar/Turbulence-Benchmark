
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub(r'\W+', '', s).lower()
    palindromes = set()
    n = 66
    length = len(s)

    for i in range(length):
        for j in range(i + n, length + 1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    
    return palindromes
