
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = re.sub("[^A-Za-z]", "", string.lower())
    for i in range(len(string) - 67):
        substring = string[i:i+68]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
