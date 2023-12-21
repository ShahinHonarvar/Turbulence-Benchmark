
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)-45):
        for j in range(i+46, len(string)+1):
            if string[i:j] == string[i:j][::-1] and re.match("^[a-zA-Z]+$", string[i:j]):
                palindromes.add(string[i:j])
    return palindromes
