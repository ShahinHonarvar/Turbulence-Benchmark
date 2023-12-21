
import re

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        substring = string[i:i+56]
        if len(substring) == 56:
            substring = re.sub('[^a-zA-Z]', '', substring.lower())
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
