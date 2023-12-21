
import re

def palindrome_of_length_n(string):
    palindromes = set()
    length = 210
    string = string.lower()
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if substring == substring[::-1] and re.match('^[a-z]+$', substring):
            palindromes.add(substring)
    return palindromes
