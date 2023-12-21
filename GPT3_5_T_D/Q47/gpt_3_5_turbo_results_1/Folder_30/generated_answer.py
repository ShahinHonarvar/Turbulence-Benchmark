
import re

def palindromes_of_specific_lengths(string):
    substr = string[14:91].lower()
    palindromes = set()
    for length in range(55, 72):
        for i in range(len(substr) - length + 1):
            palindrome = substr[i:i + length]
            if palindrome == palindrome[::-1] and re.match('^[a-zA-Z]+$', palindrome):
                palindromes.add(palindrome)
    return palindromes
