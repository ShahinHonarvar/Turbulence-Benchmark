
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string)-50):
        for j in range(i+50, len(string)+1):
            substring = string[i:j].lower()
            if substring == substring[::-1] and re.match("^[a-zA-Z]+$", substring):
                palindromes.add(substring)
    return palindromes
