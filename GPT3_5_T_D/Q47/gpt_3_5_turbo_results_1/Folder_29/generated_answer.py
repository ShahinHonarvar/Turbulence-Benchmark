
import re

def palindromes_of_specific_lengths(string):
    substring = string[15:95]
    substr_len = len(substring)
    palindrome_set = set()
  
    for length in range(18, 74):
        if length > substr_len:
            continue
        for start_index in range(substr_len - length + 1):
            palindrome = substring[start_index:start_index + length]
            palindrome = palindrome.lower()
            if re.match('^[a-zA-Z]+$', palindrome) and palindrome == palindrome[::-1]:
                palindrome_set.add(palindrome)
    
    return palindrome_set
