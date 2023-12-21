
import re

def palindromes_of_specific_lengths(string):
    substring = string[16:95].lower()
    palindromes = set()
    
    for length in range(39, 53):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i+length]
            if palindrome == palindrome[::-1] and re.match('^[a-z]+$', palindrome):
                palindromes.add(palindrome)
    
    return palindromes
