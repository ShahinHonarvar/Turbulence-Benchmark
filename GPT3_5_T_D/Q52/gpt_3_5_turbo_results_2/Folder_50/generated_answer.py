
import re

def palindrome_of_length_n(string):
    palindromes = set()
    n = 40
    for i in range(len(string) - n + 1):
        substring = string[i: i + n]
        if re.match("^[a-zA-Z]+$", substring):
            if substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes
