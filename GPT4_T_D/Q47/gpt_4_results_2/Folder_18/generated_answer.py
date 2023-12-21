
import re

def palindromes_of_specific_lengths(s):
    s = s[11:84]
    pattern = '[^a-zA-Z]'
    s = re.sub(pattern, '', s).lower()
    palindromes = set()
    for length in range(13, 67):
        for i in range(len(s)):
            substring = s[i:i+length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
