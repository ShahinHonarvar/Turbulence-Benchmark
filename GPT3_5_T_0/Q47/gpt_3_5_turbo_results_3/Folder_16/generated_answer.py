
import re

def palindromes_of_specific_lengths(string):
    substring = string[15:87]
    palindromes = set()
    
    for length in range(51, 61):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            sub = re.sub('[^a-zA-Z]', '', sub)
            if sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    
    return palindromes
