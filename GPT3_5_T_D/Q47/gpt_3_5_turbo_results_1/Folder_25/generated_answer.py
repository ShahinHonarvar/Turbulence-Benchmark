
import re

def palindromes_of_specific_lengths(string):
    substring = string[26:85].lower()
    palindromes = set()
    
    for i in range(30, 47):
        for j in range(len(substring)-i+1):
            if re.match("^[a-zA-Z]+$", substring[j:j+i]) is not None and substring[j:j+i] == substring[j:j+i][::-1]:
                palindromes.add(substring[j:j+i])
    
    return palindromes
