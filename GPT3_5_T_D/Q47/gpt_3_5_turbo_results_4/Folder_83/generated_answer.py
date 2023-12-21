
import re

def palindromes_of_specific_lengths(string):
    substring = string[75:96].lower()
    palindromes = set()
    
    for i in range(len(substring)):
        for j in range(7, 10):
            if i + j <= len(substring):
                substring_sub = substring[i:i+j]
                if substring_sub == substring_sub[::-1] and re.match("^[a-zA-Z]+$", substring_sub):
                    palindromes.add(substring_sub)
    
    return palindromes
