
import re

def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    length = 17

    for i in range(len(s) - length + 1):
        substring = s[i:i+length]
        if re.match(r'^[a-zA-Z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
