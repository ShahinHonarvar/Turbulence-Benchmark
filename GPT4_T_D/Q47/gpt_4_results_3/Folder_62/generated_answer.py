
import re

def palindromes_of_specific_lengths(s):
    s = s[26:88].lower()
    s = ''.join(re.findall(r'[a-z]', s))
    palindromes = set()

    for i in range(len(s)):
        for j in range(i+52, min(i+57, len(s)+1)):
            sub = s[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes
