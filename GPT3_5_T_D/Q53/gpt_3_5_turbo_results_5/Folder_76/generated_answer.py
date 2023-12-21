
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()

    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 136, len(string)):
            if string[i:j+1] == string[i:j+1][::-1] and re.match("^[a-zA-Z]+$", string[i:j+1]):
                palindromes.add(string[i:j+1])

    return palindromes
