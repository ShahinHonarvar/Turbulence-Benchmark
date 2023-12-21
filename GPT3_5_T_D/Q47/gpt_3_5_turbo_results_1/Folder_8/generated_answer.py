
import re

def palindromes_of_specific_lengths(string):
    string = string.lower()
    substr = string[17:73]
    palindromes = set()
    
    for i in range(len(substr)-50):
        sub = substr[i:i+51]
        sub = re.sub('[^a-zA-Z]', '', sub)
        if sub == sub[::-1]:
            palindromes.add(sub)
    
    return palindromes
