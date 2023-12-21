
import re

def palindrome_of_length_n(string):
    palindromes = set()
    cleansed_string = re.sub(r'[^a-zA-Z]', '', string.lower())

    for i in range(len(cleansed_string) - 34):
        substring = cleansed_string[i:i+35]
        if substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
