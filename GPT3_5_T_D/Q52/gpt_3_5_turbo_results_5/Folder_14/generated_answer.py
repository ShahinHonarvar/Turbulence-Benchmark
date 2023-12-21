
import re

def palindrome_of_length_n(string):
    palindromes = set()
    length = 63
    string = string.lower()
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes

def is_palindrome(substring):
    return substring == substring[::-1] and re.match('^[a-zA-Z]+$', substring)
