
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 19):
        substring = string[i:i+20]
        if re.match(r'^[a-z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
