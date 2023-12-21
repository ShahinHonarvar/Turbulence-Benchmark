
import string

def palindromes_of_specific_lengths(string):
    string = string.lower()
    string = string[34:91]
    palindromes = set()
   
    for length in range(14, 40):
        for i in range(len(string) - length + 1):
            substring = string[i:i+length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
