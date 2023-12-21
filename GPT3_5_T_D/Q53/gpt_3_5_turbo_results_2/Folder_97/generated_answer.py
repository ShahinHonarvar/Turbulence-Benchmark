
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = re.sub('[^a-zA-Z]', '', string.lower())

    for i in range(len(string)):
        for j in range(i + 138, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
