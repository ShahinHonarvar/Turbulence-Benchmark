
import re

def palindromes_of_specific_lengths(string):
    substring = string[29:99].lower()
    palindromes = set()
    for length in range(6, 10):
        for i in range(len(substring) - length + 1):
            palindrome = substring[i:i+length]
            if palindrome == palindrome[::-1] and re.match("^[a-zA-Z]+$", palindrome):
                palindromes.add(palindrome)
    return palindromes
