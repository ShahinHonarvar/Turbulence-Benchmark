
import re

def palindrome_of_length_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    string = string.lower()
    palindromes = set()
    length = 80
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
