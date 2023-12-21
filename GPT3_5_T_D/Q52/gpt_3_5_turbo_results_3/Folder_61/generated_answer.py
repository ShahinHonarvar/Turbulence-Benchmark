
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()

    for i in range(len(string)-73):
        substring = string[i:i+74]
        if re.match("^[a-z]*$", substring):
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
