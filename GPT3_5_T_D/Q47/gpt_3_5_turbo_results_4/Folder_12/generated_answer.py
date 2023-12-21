
import re

def palindromes_of_specific_lengths(string):
    substring = string[62:89].lower()
    palindromes = set()
    
    for i in range(len(substring)):
        for j in range(i+18, i+22):
            if j <= len(substring):
                sub = substring[i:j]
                if sub == sub[::-1] and re.match("^[a-zA-Z]+$", sub):
                    palindromes.add(sub)
    
    return palindromes
