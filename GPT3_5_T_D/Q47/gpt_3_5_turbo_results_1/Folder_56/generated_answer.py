
import string

def palindromes_of_specific_lengths(str):
    str = str.lower()
    palindromes = set()
    
    for i in range(1, 10):
        substring = str[i:10]
        
        for length in range(3, 8):
            if len(substring) >= length:
                substr = substring[:length]
                
                if substr.isalpha():
                    if substr == substr[::-1]:
                        palindromes.add(substr)
    
    return palindromes
