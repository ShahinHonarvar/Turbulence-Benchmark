
import re

def palindromes_of_specific_lengths(string):
    substring = string[75:96]
    palindromes = set()
    
    for length in range(7, 10):
        # Find all substrings of specified length
        substrings = re.findall('[a-zA-Z]{%d}' % length, substring)
        
        for substring in substrings:
            # Check if substring is a palindrome in a case-insensitive manner
            if substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    
    return palindromes
