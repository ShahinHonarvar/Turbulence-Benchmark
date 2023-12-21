
import re

def palindromes_of_specific_lengths(string):
    substring = string[26:85].lower()
    palindromes = set()

    for length in range(30, 47):
        for i in range(len(substring) - length + 1):
            temp = substring[i:i+length]
            if temp == temp[::-1] and re.match("^[a-zA-Z]+$", temp):
                palindromes.add(temp)

    return palindromes
