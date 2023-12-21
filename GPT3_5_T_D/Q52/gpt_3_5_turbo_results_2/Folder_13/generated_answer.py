
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 205):
        substring = string[i:i+206]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
