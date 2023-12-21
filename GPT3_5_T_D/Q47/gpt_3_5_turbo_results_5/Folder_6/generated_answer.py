
import string

def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(45, 99):
        for j in range(40, 48):
            substring = string[i:i+j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
