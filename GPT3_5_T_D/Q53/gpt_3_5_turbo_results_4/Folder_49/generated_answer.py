
import re

def palindrome_of_length_at_least_n(string):
    patterns = []
    for i in range(73, len(string) + 1):
        patterns.append(r'(?i)(\b\w{%d}\b)' % i)
    results = set()
    for pattern in patterns:
        results.update(re.findall(pattern, string))
    return results
