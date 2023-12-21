
import re

def palindrome_of_length_n(string):
    palindrome_set = set()
    string = string.lower()
    pattern = r'[a-zA-Z]{17}'
    matches = re.findall(pattern, string)
    
    for match in matches:
        if match == match[::-1]:
            palindrome_set.add(match)
    
    return palindrome_set
