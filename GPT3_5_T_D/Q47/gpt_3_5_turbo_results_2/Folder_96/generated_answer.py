
import re

def palindromes_of_specific_lengths(string):
    substr = string[100:301]
    substr = re.sub('[^A-Za-z]', '', substr)
    substr = substr.lower()
    
    palindromes = set()
    
    for i in range(len(substr) - 99):
        for j in range(50, 101):
            if substr[i:i+j] == substr[i:i+j][::-1]:
                palindromes.add(substr[i:i+j])
    
    return palindromes
