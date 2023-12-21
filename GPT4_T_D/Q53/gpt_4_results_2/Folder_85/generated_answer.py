
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub(r'\W+', '', s).lower()
    n = 85
    len_s = len(s)
    res = set()

    for i in range(n, len_s + 1):
        for j in range(0, len_s - i + 1):
            substr = s[j:j + i]
            if substr == substr[::-1]:
                res.add(substr)

    return res
