
import re

def palindromes_of_specific_lengths(s):
    s = s[23:83]
    palindromes = set()
    for i in range(len(s) - 31):
        for j in range(i + 32, min(i + 35, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                substring = re.sub('[^a-zA-Z]', '', substring)
                if len(substring) >= 32 and len(substring) <= 34:
                    palindromes.add(substring.lower())
    return palindromes
