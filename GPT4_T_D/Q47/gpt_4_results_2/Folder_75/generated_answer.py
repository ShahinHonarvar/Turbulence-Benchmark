
import re

def palindromes_of_specific_lengths(s):
    s = s[31:75].lower()
    pal_set = set()
    for i in range(len(s)):
        for j in range(23, min(40, len(s) - i + 1)):
            substr = s[i:i + j]
            if substr == substr[::-1] and substr.isalpha():
                pal_set.add(substr)
    return pal_set
