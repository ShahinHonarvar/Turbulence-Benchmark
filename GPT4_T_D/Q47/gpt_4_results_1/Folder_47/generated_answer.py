
import re

def palindromes_of_specific_lengths(s):
    s = s[39:95]
    s = re.sub(r'[^a-zA-Z]', '', s)
    s = s.lower()
    palindromes = set()

    for start in range(len(s)):
        for end in range(start+14, min(start+53, len(s)+1)):
            substring = s[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
