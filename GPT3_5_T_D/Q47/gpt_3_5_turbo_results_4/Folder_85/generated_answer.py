
import string

def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(29, 99):
        substr = string[i:i+10]
        if len(substr) in range(6, 10):
            substr = ''.join(filter(str.isalpha, substr)).lower()
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
