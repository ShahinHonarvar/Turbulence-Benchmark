
import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-z]+', '', s.lower())
    palindromes = set()
    length = len(s) 

    for i in range(length):
        for j in range(i + 92, length + 1):
            substring = s[i:j]
            if substring == substring[::-1]: 
                palindromes.add(substring)
                
    return palindromes
