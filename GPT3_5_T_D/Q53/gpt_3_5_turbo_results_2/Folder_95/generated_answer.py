
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub(r'[^a-zA-Z]', '', s).lower()
    result = set()
    for i in range(len(s)-34):
        for j in range(i+35, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                result.add(s[i:j])
    return result
