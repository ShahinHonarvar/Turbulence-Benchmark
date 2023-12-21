
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-z]+', '', s.lower())
    n = 140
    results = set()

    for i range(len(s)):
        for j range(i + n - 1, len(s)):
            sub = s[i:j+1]
            if sub == sub[::-1]:
                results.add(sub)
    return results
