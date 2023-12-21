
import re

def palindrome_of_length_at_least_n(s):
    result = set()
    s = re.sub('[^a-zA-Z]', '', s.lower())
    
    for i in range(len(s)):
        for j in range(i + 55, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    
    return result
