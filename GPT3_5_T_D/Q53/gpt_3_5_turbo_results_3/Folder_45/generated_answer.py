
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = re.sub("[^a-zA-Z]", "", string.lower())

    for i in range(len(string) - 46):
        substring = string[i:i+47]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
