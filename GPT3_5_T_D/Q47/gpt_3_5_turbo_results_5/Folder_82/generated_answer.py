
import re

def palindromes_of_specific_lengths(string):
    substring = string[3:301]
    
    result = set()
    for length in range(30, 301):
        regex = r'(?i)([a-zA-Z])' + r'\S' * (length - 2) + r'\1'
        matches = re.findall(regex, substring)
        for match in matches:
            result.add(match.lower())
    
    return result
