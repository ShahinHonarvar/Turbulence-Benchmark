
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub(r"[^a-zA-Z]", "", s)
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            if j - i + 1 >= 56:
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    result.add(substring)
    return result
