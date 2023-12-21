
import re

def palindrome_of_length_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    length_n_palindromes = set()
    for i in range(len(string) - 444):
        substring = string[i:i+445]
        if substring == substring[::-1]:
            length_n_palindromes.add(substring)
    return length_n_palindromes
