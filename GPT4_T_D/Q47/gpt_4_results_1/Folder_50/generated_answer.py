
import re

def palindromes_of_specific_lengths(s):
    s = s[36:93].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+10, min(i+36, len(s)+1)):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes
