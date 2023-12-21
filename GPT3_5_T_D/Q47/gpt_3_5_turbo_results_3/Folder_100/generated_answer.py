
import re

def palindromes_of_specific_lengths(string):
    substring = string[29:97].lower()
    palindromes = set()
    
    for length in range(12, 19):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if re.match("^[a-zA-Z]+$", sub):
                if sub == sub[::-1]:
                    palindromes.add(sub)
    
    return palindromes
