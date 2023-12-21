
import re

def palindromes_of_specific_lengths(s):
    s = s[26:88].lower()
    valid_palindromes = set()

    for i in range(len(s)):
        for j in range(52, 57):
            if i + j > len(s):
                break
            substring = s[i:i + j]
            if substring == substring[::-1] and re.match("^[a-z]+$", substring):
                valid_palindromes.add(substring)
    
    return valid_palindromes
