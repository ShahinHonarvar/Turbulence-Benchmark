
import re

def palindromes_of_specific_lengths(string):
    substring = string[43:96]
    substring = re.sub(r'[^a-zA-Z]', '', substring)
    substring = substring.lower()
    
    palindromes = set()
    
    for i in range(len(substring)):
        for j in range(i + 18, min(i + 48, len(substring) + 1)):
            sub = substring[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    
    return palindromes
