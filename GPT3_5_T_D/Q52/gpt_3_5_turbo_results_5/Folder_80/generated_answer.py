
import re

def palindrome_of_length_n(string):
    n = 276
    substrings = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if re.match('^[a-zA-Z]+$', substring):
            if substring.lower() == substring.lower()[::-1]:
                substrings.add(substring)
    
    return substrings
