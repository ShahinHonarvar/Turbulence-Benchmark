
import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    n = 112
    for i in range(n, len(s)+1):
        for j in range(len(s)-i+1):
            substring = s[j:j+i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
