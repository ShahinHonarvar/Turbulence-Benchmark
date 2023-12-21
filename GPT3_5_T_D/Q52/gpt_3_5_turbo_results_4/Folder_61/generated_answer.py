
import string

def palindrome_of_length_n(string):
    n = 74
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
