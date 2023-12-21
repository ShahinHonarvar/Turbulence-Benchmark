
import re

def palindrome_of_length_n(string):
    string = re.sub("([^a-zA-Z])", "", string.lower())
    palindromes = set()
    for i in range(len(string)-14):
        substring = string[i:i+15]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
