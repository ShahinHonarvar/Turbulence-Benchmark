
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub(r'[^A-Za-z]', '', s).lower()
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + 54, length + 1):
            fragment = s[i:j]
            if fragment == fragment[::-1]:
                palindromes.add(fragment)
    return palindromes
