
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub(r'\W+', '', s).lower()
    results = set()
    for i in range(len(s)):
        for j in range(i + 27, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                results.add(s[i:j])
    return results
