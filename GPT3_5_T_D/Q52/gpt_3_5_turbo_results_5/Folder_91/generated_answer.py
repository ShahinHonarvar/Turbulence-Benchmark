
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 6):
        substring = string[i:i+7]
        if re.match("^[a-z]*$", substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
