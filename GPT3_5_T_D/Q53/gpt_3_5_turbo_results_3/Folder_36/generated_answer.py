
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i + 144, len(string) + 1):
            substring = string[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes

def is_palindrome(string):
    if re.match('^[a-zA-Z]+$', string):
        return string == string[::-1]
    return False
