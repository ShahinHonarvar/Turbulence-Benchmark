
import re

def palindromes_of_specific_lengths(string):
    substring = string[15:95]
    substring = re.sub('[^a-zA-Z]', '', substring)
    substring = substring.lower()
    palindromes = set()
    
    for length in range(18, 74):
        for start in range(len(substring) - length + 1):
            end = start + length
            sub = substring[start:end]
            if sub == sub[::-1]:
                palindromes.add(sub)
    
    return palindromes
