
import re

def palindromes_of_specific_lengths(string):
    string = string.lower()
    substring = string[12:123]
    palindromes = set()

    for length in range(12, 221):
        for index in range(len(substring) - length + 1):
            word = substring[index:index+length]
            if re.match(r'^[a-z]+$', word) and word == word[::-1]:
                palindromes.add(word)

    return palindromes
