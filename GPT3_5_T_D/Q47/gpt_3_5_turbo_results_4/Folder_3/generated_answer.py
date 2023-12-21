
import string

def palindromes_of_specific_lengths(string):
    palindromes = set()
    string = string.lower()
    
    for i in range(27, 96):
        for length in range(49, 52):
            substring = string[i:i+length]
            
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
