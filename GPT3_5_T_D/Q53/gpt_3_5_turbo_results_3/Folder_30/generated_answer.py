
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+16, len(string)+1):
            substring = string[i:j]
            if substring == substring[::-1]:
                if re.match('^[a-z]+$', substring, re.IGNORECASE):
                    palindromes.add(substring)
    return palindromes
