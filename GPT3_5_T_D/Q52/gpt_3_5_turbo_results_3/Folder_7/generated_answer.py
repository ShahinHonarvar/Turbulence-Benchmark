
import re

def palindrome_of_length_n(string):
    length_n_palindromes = set()
    string = re.sub('[^a-zA-Z]', '', string)
    length = 416

    for i in range(len(string) - length + 1):
        substr = string[i:i+length].lower()
        if substr == substr[::-1]:
            length_n_palindromes.add(substr)

    return length_n_palindromes
