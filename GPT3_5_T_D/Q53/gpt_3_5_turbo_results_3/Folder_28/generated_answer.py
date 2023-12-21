
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i, len(string)):
            p = string[i:j+1]
            if len(p) >= 42 and p == p[::-1] and re.match("^[a-zA-Z]+$", p):
                palindromes.add(p)
    return palindromes
