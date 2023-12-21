
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub(r'[^a-zA-Z]', '', s)
    s = s.lower()
    palindromes = set()
    for i in range(len(s)-67):
        substring = s[i:i+68]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
