
import re

def palindromes_of_specific_lengths(text):
    pallindromes = set()
    substring = text[32:80]
    
    for l in range(35, 42):
      for i in range(len(substring)-l+1):
        strs = substring[i:i+l]
        if strs == strs[::-1] and re.match("^[A-Za-z]*$", strs):
          pallindromes.add(strs.lower())
    return pallindromes
