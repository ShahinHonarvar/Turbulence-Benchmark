
import re

def palindromes_of_specific_lengths(string):
    string = string[70:141]
    string = string.lower()
    palindromes = set()
    for length in range(3, 61):
        for start in range(len(string) - length + 1):
            substring = string[start:start + length]
            if re.match(r'^[a-zA-Z]+$', substring):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes
