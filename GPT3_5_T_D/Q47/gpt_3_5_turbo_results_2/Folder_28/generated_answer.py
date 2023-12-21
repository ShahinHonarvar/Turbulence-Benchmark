
import re

def palindromes_of_specific_lengths(string):
    substring = string[32:72].lower()
    palindromes = set()

    for length in range(21, 33):
        for i in range(len(substring) - length + 1):
            substring_slice = substring[i:i+length]
            
            if substring_slice.isalpha() and substring_slice == substring_slice[::-1]:
                palindromes.add(substring_slice)

    return palindromes
