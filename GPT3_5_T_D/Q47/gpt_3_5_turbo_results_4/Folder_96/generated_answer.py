
import re

def palindromes_of_specific_lengths(string):
    substring = string[100:301]
    substring = re.sub(r'[^a-zA-Z]', '', substring).lower()
    palindromes = set()
    
    for i in range(50, 101):
        for j in range(len(substring) - i + 1):
            sub = substring[j : j + i]
            if sub == sub[::-1]:
                palindromes.add(sub)
    
    return palindromes
