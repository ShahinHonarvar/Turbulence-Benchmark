
import re

def palindromes_of_specific_lengths(s):
    s = s[16:78]
    s = re.sub('[^a-z]+', '', s.lower())
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+43, min(i+48, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
