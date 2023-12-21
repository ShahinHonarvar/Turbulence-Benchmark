
import string

def palindromes_of_specific_lengths(string):
    palindromes = set()
    
    for i in range(8):
        for j in range(i+4, min(i+6, 8)):
            substring = string[i:j+1]
            
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    
    return palindromes
