
import re

def palindromes_of_specific_lengths(string):
    substring = string[70:141]
    palindromes = set()
    
    for length in range(3, 61):
        for start in range(len(substring) - length + 1):
            end = start + length
            palindrome = substring[start:end].lower()
            
            if re.match('^[a-z]+$', palindrome) and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    
    return palindromes
