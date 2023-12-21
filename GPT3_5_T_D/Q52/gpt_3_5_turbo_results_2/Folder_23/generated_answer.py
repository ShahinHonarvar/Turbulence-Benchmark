
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 68):
        sub = string[i:i+69]
        if re.match(r"^[a-zA-Z]+$", sub) and sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes
