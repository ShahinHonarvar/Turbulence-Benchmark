
import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[:301]
    substring = re.sub('[^a-zA-Z]', '', substring.lower())
    
    for i in range(len(substring) - 50):
        for j in range(50, 61):
            if substring[i:i+j] == substring[i:i+j][::-1]:
                palindromes.add(substring[i:i+j])
    
    return palindromes
