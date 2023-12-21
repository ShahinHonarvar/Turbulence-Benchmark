
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()

    for i in range(len(string)-94):
        substring = string[i:i+95]

        if re.match("^[a-z]+$", substring) and substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
