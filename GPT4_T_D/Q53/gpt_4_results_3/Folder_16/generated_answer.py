
import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = re.sub('[^a-z]', '', s)
    
    palindromes = set()

    for i in range(len(s)):
        for j in range(i+119, len(s)+1):
            sub_str = s[i:j]
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
                
    return palindromes
