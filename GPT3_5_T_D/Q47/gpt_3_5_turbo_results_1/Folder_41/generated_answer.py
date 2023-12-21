
import re

def palindromes_of_specific_lengths(string):
    substring = string[1:8].lower()
    palindromes = set()

    for length in range(3, 5):
        for i in range(len(substring) - length + 1):
            word = substring[i:i+length]

            if word == word[::-1] and re.match("^[a-zA-Z]+$", word):
                palindromes.add(word)

    return palindromes
