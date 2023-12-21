
import re

def palindrome_of_length_n(string):
    palindromes = set()

    # convert the string to lowercase
    string = string.lower()

    # find all substrings of length 464
    substrings = re.findall(f'(?=([a-zA-Z]{{464}}))', string)

    # check if each substring is a palindrome
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
