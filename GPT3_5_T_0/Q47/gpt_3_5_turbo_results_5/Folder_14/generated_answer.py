
import re

def palindromes_of_specific_lengths(string):
    substring = string[10:75]
    substring = re.sub('[^a-zA-Z]', '', substring)
    substring = substring.lower()
    palindromes = set()
    
    for length in range(6, 9):
        for i in range(len(substring) - length + 1):
            if substring[i:i+length] == substring[i:i+length][::-1]:
                palindromes.add(substring[i:i+length])
    
    return palindromes
