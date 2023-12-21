
import re

def palindrome_of_length_n(string):
    palindromes = set()

    string = string.lower()
    string = re.sub("[^a-z]", "", string)

    for i in range(len(string) - 82):
        substring = string[i:i+83]
        if substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
