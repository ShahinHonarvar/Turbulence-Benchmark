
import re

def palindromes_of_specific_lengths(string):
    substring = string[26:91]
    palindrome_set = set()

    for length in range(27, 59): 
        for i in range(len(substring) - length + 1): 
            sub = substring[i:i+length]
            sub_lower = re.sub(r'[^a-zA-Z]', '', sub.lower())
            if sub_lower == sub_lower[::-1]:
                palindrome_set.add(sub_lower)
    
    return palindrome_set
