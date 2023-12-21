
import re

def palindromes_of_specific_lengths(string):
    string = string.lower()
    substring = string[10:75]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(6, 9):
            sub = substring[i:i+j]
            if is_palindrome(sub):
                palindromes.add(sub)
    
    return palindromes

def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z]', '', s)
    return s == s[::-1]
