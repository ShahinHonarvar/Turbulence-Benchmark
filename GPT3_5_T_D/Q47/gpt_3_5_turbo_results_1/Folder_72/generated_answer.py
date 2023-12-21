
import re

def palindromes_of_specific_lengths(string):
    substr = string[26:91]
    substr = re.sub('[^a-zA-Z]', '', substr)
    substr = substr.lower()
    
    palindromes = set()
    for length in range(27, 59):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i+length]
            if sub == sub[::-1]:
                palindromes.add(sub)
    
    return palindromes
