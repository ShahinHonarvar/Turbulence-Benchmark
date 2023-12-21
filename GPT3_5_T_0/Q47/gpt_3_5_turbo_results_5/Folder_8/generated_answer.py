
import re

def palindromes_of_specific_lengths(string):
    substring = string[17:73].lower()
    palindromes = set()
    
    for i in range(len(substring) - 50):
        for j in range(50, 52):
            if re.match(r'^[a-zA-Z]+$', substring[i:i+j]) and substring[i:i+j] == substring[i:i+j][::-1]:
                palindromes.add(substring[i:i+j])
    
    return palindromes
