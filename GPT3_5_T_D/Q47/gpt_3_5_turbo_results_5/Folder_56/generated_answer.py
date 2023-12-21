
import re

def palindromes_of_specific_lengths(string):
    string = string[1:10].lower()
    palindromes = set()

    for length in range(3, 8):
        for start in range(len(string) - length + 1):
            substring = string[start:start+length]

            if re.match(r'^[a-zA-Z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
