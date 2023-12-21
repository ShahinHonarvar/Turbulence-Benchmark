
import string

def palindrome_of_length_n(s):
    if len(s) < 57:
        return set()
    
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 56):
        substring = s[i:i+57]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
