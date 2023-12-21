
import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    processed_s = "".join(re.findall("[a-zA-Z]*", s))
    
    length = len(processed_s)
    
    for i in range(length):
        for j in range(i + 55, length):
            substring = processed_s[i:j+1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
