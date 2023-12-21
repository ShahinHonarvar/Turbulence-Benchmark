
import re

def palindromes_of_specific_lengths(string):
    substring = string[200:301].lower()
    palindromes = set()
    
    for length in range(10, 51):
        for index in range(len(substring) - length + 1):
            sub = substring[index:index+length]
            if re.match("^[a-zA-Z]+$", sub):
                if sub == sub[::-1]:
                    palindromes.add(sub)
    
    return palindromes
