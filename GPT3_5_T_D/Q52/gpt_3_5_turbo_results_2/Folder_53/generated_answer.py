
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    length = 68
    for i in range(len(string) - length + 1):
        sub = string[i:i+length]
        if re.match(r'^[a-zA-Z]+$', sub):
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes
