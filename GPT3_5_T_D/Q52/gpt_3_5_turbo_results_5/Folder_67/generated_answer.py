
import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)-41):
        substring = s[i:i+42]
        if re.match(r'^[a-z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
