
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+21, len(string)):
            substring = string[i:j+1]
            if substring == substring[::-1] and re.fullmatch('[a-zA-Z]+', substring):
                palindromes.add(substring)
    return palindromes
