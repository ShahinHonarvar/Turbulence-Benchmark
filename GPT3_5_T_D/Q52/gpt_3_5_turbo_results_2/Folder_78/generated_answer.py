
import re

def palindrome_of_length_n(string):
    string = string.lower()
    pattern = '[a-zA-Z]{48}'
    palindromes = re.findall(pattern, string)
    return set(palindromes)
