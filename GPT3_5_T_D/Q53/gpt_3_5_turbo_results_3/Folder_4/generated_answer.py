
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    string = string.lower()

    palindromes = set()
    for i in range(len(string)):
        for j in range(i+99, len(string)+1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
