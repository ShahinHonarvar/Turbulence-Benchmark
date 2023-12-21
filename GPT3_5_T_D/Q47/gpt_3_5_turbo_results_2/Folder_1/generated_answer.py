
import re

def palindromes_of_specific_lengths(string):
    substring = string[15:90]
    palindromes = set()
    
    for i in range(40, 73):
        regex = r"(?i)([a-zA-Z]{" + str(i) + r"})(?=\1[::-1])"
        matches = re.findall(regex, substring)
        palindromes.update(matches)
    
    return palindromes
