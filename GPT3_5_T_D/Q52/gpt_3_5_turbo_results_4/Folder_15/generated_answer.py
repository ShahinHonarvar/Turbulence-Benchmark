
import re

def palindrome_of_length_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    palindromes = set()
    length = 4

    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)

    return palindromes
