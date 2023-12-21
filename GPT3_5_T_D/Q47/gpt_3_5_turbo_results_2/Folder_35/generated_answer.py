
import re

def palindromes_of_specific_lengths(string):
    substring = string[34:91].lower()
    palindrome_set = set()
    
    for length in range(14, 40):
        for i in range(len(substring) - length + 1):
            substring_part = substring[i:i+length]
            if substring_part == substring_part[::-1] and re.match("^[a-z]+$", substring_part):
                palindrome_set.add(substring_part)
    
    return palindrome_set
