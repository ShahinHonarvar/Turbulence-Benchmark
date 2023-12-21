
import re

def palindromes_of_specific_lengths(string):
    substr = string[1:300].lower()
    palindromes = set()
  
    for length in range(3, 11):
        for i in range(0, len(substr) - length + 1):
            substring = substr[i:i+length]
            if re.match('^[a-zA-Z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
  
    return palindromes
