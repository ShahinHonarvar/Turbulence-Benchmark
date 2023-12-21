
import re

def palindromes_of_specific_lengths(string):
    substring = string[127:289].lower()
    palindromes = set()
    
    for length in range(119, 142):
        for index in range(len(substring) - length + 1):
            sub = substring[index:index+length]

            if re.match(r'^[a-zA-Z]+$', sub) and sub == sub[::-1]:
                palindromes.add(sub)
    
    return palindromes
