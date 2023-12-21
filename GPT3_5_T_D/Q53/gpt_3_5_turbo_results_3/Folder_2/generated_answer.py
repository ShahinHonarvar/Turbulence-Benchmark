
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub(r'[^a-zA-Z]', '', s.lower())
    result = set()
    n = len(s)
    
    for i in range(n):
        for j in range(i + 55, n + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                result.add(sub)
    
    return result
