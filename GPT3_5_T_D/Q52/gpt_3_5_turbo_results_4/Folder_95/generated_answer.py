
import re

def palindrome_of_length_n(string):
    palindromes = set()
    substrings = re.findall(r'[a-zA-Z]+', string)
    for substring in substrings:
        if len(substring) == 87:
            palindrome = substring.lower()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
