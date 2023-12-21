
import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = re.sub('[^a-z]', '', s)
    length = len(s)
    palindromes = set()
    
    for l in range(44, length + 1):
        for i in range(length - l + 1):
            candidate = s[i: i + l]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
                
    return palindromes
