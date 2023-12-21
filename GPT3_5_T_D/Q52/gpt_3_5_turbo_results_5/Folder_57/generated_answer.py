
import re

def palindrome_of_length_n(string):
    if len(string) < 92:
        return set()
    string = string.lower()
    palindromes = set()
    for i in range(len(string)-91):
        substring = string[i:i+92]
        if re.match("^[a-zA-Z]*$", substring) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
