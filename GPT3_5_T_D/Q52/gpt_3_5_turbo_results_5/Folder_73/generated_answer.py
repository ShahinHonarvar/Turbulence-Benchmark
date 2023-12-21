
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes_set = set()
    for i in range(len(string)-40):
        substring = string[i:i+41]
        if re.match('^[a-zA-Z]+$', substring):
            if substring == substring[::-1]:
                palindromes_set.add(substring)
    return palindromes_set
