
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    lowercase_string = string.lower()
    for i in range(len(lowercase_string)):
        for j in range(i+35, len(lowercase_string)+1):
            substring = lowercase_string[i:j]
            if re.match("^[a-z]+$", substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
