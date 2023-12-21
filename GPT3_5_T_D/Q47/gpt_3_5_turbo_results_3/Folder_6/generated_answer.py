
import re

def palindromes_of_specific_lengths(string):
    substr = string[45:99]
    substr = substr.lower()
    substr = re.findall('[a-zA-Z]+', substr)
    
    palindromes = set()
    for word in substr:
        for i in range(40, 48):
            if word[:i] == word[:i][::-1]:
                palindromes.add(word[:i])
    
    return palindromes
