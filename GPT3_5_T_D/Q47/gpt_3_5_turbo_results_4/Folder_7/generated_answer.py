
import re

def palindromes_of_specific_lengths(string):
    substring = string[119:257].lower()
    palindromes = set()
    
    for length in range(104, 124):
        for start in range(len(substring) - length + 1):
            sub_str = substring[start:start+length]
            if sub_str == sub_str[::-1] and re.match('^[a-zA-Z]+$', sub_str):
                palindromes.add(sub_str)
    
    return palindromes
