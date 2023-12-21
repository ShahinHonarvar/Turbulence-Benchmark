
import re

def palindromes_of_specific_lengths(s):
    s = s[11:88].lower()
    s = re.sub('[^a-z]', '', s)

    palindromes = set()
    for i in range(len(s)):
        for j in range(i+4, min(i+6, len(s)+1)):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])

    return palindromes
