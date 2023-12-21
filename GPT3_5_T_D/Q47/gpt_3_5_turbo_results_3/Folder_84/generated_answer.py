
import string

def palindromes_of_specific_lengths(string):
    substring = string[23:78].lower()
    palindromes = set()
    
    for length in range(13, 41):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
                
    return palindromes
