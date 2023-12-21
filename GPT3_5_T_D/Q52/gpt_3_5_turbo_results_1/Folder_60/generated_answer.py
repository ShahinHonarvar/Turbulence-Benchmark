
import string

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 87):
        substring = string[i:i+88]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
