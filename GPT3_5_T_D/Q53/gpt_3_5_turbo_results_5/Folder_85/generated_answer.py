
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^A-Za-z]+', '', string)
    string = string.lower()
    palindromes = set()

    for i in range(len(string) - 84):
        for j in range(i + 85, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
