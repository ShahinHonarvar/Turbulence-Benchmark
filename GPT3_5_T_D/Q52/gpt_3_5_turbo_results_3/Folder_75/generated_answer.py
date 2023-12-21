
import re

def palindrome_of_length_n(string):
    string = string.lower()
    length = 80
    palindromes = set()
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if re.match("^[a-zA-Z]+$", substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
