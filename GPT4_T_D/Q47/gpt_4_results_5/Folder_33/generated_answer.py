
import string

def is_palindrome(s):
    return s == s[::-1]

def is_alpha(s):
    return all(c in string.ascii_lowercase for c in s)

def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[130:296]
    
    palindromes = set()
    for length in range(103, 159):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring) and is_alpha(substring):
                palindromes.add(substring)
                
    return palindromes
