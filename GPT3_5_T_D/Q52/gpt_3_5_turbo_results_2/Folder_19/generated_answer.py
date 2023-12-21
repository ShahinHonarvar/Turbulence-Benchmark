
import re

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 66):
        substring = string[i:i+67]
        if re.match("^[a-zA-Z]+$", substring):
            if substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes
