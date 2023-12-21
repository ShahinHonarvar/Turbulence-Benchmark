
import re

def palindromes_of_specific_lengths(string):
    substring = string[15:73].lower()
    palindromes_set = set()
    
    for length in range(19, 56):
        regex = r"(?=(\b\w{%d}\b))" % length
        matches = re.findall(regex, substring)
        
        for match in matches:
            if match == match[::-1]:
                palindromes_set.add(match)
    
    return palindromes_set
