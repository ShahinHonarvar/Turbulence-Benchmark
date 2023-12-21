
import string

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)-53):
        for j in range(54, len(string)-i+1):
            substring = string[i: i+j]
            if substring == substring[::-1] and all(letter in string.ascii_letters for letter in substring):
                palindromes.add(substring)
    return palindromes
