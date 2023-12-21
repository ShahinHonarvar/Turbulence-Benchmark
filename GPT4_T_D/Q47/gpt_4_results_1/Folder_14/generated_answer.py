
import re

def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[10:75]
    s = re.sub('[^a-z]', '', s)
    results = set()
    for length in range(6, 9):
        for i in range(len(s)):
            sub_s = s[i: i+length]
            if sub_s == sub_s[::-1]:
                results.add(sub_s)
    return results
