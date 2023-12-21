
import re

def palindromes_of_specific_lengths(s):
    s = s[11:84]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start, len(s)):
            sub = s[start:end+1]
            if 13 <= len(sub) <= 66 and sub.lower() == sub[::-1].lower() and re.match('^[a-zA-Z]*$', sub):
                palindromes.add(sub)
    return palindromes
