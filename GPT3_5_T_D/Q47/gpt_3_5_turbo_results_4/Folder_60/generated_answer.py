
import re

def palindromes_of_specific_lengths(string):
    substring = string[23:83].lower()
    palindromes = set()
    
    for i in range(len(substring)-1):
        for j in range(i+1, min(i+35, len(substring))):
            if j - i + 1 in range(32, 35) and re.match("^[a-zA-Z]*$", substring[i:j+1]):
                if substring[i:j+1] == substring[i:j+1][::-1]:
                    palindromes.add(substring[i:j+1])
    
    return palindromes
