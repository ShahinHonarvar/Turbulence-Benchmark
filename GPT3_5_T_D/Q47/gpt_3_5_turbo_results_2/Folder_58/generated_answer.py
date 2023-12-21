
import re

def palindromes_of_specific_lengths(string):
    substring = string[125:284]
    
    palindromes = set()
    
    for length in range(109, 127):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            substr = re.sub('[^a-zA-Z]', '', substr)
            
            if substr.lower() == substr.lower()[::-1]:
                palindromes.add(substr)
    
    return palindromes
