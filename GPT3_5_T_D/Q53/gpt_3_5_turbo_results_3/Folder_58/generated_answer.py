
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string) - 146):
        substring = string[i: i + 147].lower()
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
