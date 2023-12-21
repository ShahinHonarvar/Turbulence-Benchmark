
import re

def palindromes_of_specific_lengths(string):
  substring = string[36:93].lower()  
  palindromes = set()

  for length in range(10, 36+1):
    for i in range(len(substring) - length + 1):
      substring_snippet = substring[i:i+length]
      if re.match("^[a-zA-Z]+$", substring_snippet) and substring_snippet == substring_snippet[::-1]:
        palindromes.add(substring_snippet)
    
  return palindromes
