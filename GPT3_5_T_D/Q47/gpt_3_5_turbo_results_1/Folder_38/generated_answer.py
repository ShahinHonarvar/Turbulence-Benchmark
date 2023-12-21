
import string

def palindromes_of_specific_lengths(string):
    palindromes = set()
    string = string.lower()
    
    for i in range(18, 88):
        substr = string[i:i+38]
        if len(substr) < 38:
            break
        if all(c in string.ascii_lowercase for c in substr):
            if substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
