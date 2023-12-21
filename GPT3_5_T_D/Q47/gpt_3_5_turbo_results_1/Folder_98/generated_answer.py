
import re

def palindromes_of_specific_lengths(string):
    string = string[:21].lower()

    palindromes = set()

    for length in range(5, 81):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1] and re.match(r'^[a-zA-Z]+$', substring):
                palindromes.add(substring)

    return palindromes
