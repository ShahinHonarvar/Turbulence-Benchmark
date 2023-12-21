
import re

def palindromes_of_specific_lengths(string):
    substring = string[10:76].lower()
    palindromes = set()
    for length in range(10, 21):
        for start in range(len(substring) - length + 1):
            palindrome = substring[start:start+length]
            if palindrome == palindrome[::-1] and re.match('^[a-zA-Z]+$', palindrome):
                palindromes.add(palindrome)
    return palindromes
