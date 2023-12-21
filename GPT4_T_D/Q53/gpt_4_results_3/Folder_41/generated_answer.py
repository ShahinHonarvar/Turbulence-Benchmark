
import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = re.sub('[^a-z]', '', s)
    res = set()
    for i in range(len(s)):
        for j in range(i + 28, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1]:
                res.add(subs)
    return res
