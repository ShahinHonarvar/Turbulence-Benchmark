
import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s.lower())
    palindromes = set()
    if len(s) >= 318:
        for i in range(len(s) - 318 + 1):
            substring = s[i:i+318]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
