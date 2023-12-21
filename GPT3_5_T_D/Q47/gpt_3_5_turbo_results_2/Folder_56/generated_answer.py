
import re

def palindromes_of_specific_lengths(s):
    s = s[1:10].lower()
    palindromes = set()
  
    for length in range(3, 8):
        for i in range(len(s) - length + 1):
            substr = s[i:i+length]
            if substr == substr[::-1] and re.match("^[a-zA-Z]+$", substr):
                palindromes.add(substr)
  
    return palindromes
