
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 99, len(string) + 1):
            substring = string[i:j]
            if re.match("^[a-zA-Z]+$", substring) and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes
