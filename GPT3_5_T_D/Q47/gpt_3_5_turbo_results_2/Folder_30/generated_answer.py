
import re

def palindromes_of_specific_lengths(s):
    s = s[14:91].lower()
    palindromes = set()
    
    for i in range(len(s)):
        for j in range(i + 55, i + 72):
            substring = s[i:j+1]
            if substring == substring[::-1] and re.match("^[a-zA-Z]+$", substring):
                palindromes.add(substring)
    
    return palindromes
