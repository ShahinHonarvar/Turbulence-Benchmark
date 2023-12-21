
import re

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 83):
        substring = string[i:i+84]
        substring = re.sub(r'[^a-zA-Z]', '', substring).lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
