
import re

def palindrome_of_length_at_least_n(s):
    result = set()
    s = re.sub(r'[^a-zA-Z]', '', s.lower())
    
    for i in range(len(s) - 25):
        substring = s[i:i+26]
        if substring == substring[::-1]:
            result.add(substring)
    
    return result
