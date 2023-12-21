
import re

def palindromes_of_specific_lengths(string):
    str_slice = string[12:57].lower()
    palindromes = set()
    
    for length in range(20, 22):
        for i in range(len(str_slice) - length + 1):
            substring = str_slice[i:i+length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
