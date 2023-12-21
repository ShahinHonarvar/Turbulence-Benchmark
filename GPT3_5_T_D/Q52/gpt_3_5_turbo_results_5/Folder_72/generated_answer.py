
import string

def palindrome_of_length_n(string):
    palindromes = set()
    n = 16
    string = string.lower()
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring == substring[::-1] and all(char in string.ascii_lowercase for char in substring):
            palindromes.add(substring)
    return palindromes
