
import re

def palindromes_of_specific_lengths(string):
    substring = string[30:85].lower()
    palindromes = set()
  
    for i in range(len(substring)):
        for j in range(12, 21):
            if i+j > len(substring):
                break
            sub = substring[i:i+j]
            if sub == sub[::-1] and re.match("^[a-zA-Z]+$", sub):
                palindromes.add(sub)
  
    return palindromes
