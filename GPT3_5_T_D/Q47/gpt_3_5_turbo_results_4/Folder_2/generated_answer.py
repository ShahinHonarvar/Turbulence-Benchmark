
import re

def palindromes_of_specific_lengths(string):
    substring = string[10:60].lower()
    palindromes = set()
    for length in range(18, 37):
        for i in range(len(substring) - length + 1):
            word = substring[i:i+length]
            if re.match("^[a-zA-Z]+$", word):
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes
