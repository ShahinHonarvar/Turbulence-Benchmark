
import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    
    for i in range(len(s)-12):
        for j in range(13, len(s)-i+1):
            sub_str = s[i:i+j]
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
    
    return palindromes
