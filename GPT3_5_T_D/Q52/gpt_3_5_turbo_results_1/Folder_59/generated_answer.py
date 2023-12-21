
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)-38):
        substring = string[i:i+39]
        if re.search(r'^[a-zA-z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
