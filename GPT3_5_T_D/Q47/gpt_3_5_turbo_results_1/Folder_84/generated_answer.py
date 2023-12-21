
import string

def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(23, 78):
        for length in range(13, 41):
            substring = string[i:(i+length)]
            if len(substring) != length:
                break
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
                
    return palindromes
