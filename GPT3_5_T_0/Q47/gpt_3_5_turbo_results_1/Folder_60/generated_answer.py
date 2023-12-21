
import re

def palindromes_of_specific_lengths(string):
    substring = string[23:83]
    substring = re.sub('[^a-zA-Z]', '', substring)
    substring = substring.lower()
    palindromes = set()
    
    for i in range(len(substring) - 34):
        for j in range(32, 35):
            if substring[i:i+j] == substring[i:i+j][::-1]:
                palindromes.add(substring[i:i+j])
    
    return palindromes
