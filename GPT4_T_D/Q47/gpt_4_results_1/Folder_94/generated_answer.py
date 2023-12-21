
import re

def palindromes_of_specific_lengths(s):
    s = s[40:95]
    s = re.sub('[^A-Za-z]', '', s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(45, min(i + 52, len(s) + 1)):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower() and 45<= len(substring) <=51:
                palindromes.add(substring)
    return palindromes
