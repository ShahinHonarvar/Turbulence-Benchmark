
import re

def palindromes_of_specific_lengths(s):
    substring = s[127:289].lower()
    palindromes = set()
    
    for length in range(119, 142):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if re.match('^[a-zA-Z]+$', sub) and sub == sub[::-1]:
                palindromes.add(sub)
    
    return palindromes
