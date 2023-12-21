
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+9, len(string)+1):
            substring = string[i:j]
            if all(re.match(r'[a-z]', char) for char in substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
