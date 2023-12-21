
import re

def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for i in range(1, 8):
        if i + 3 <= 8:
            substring = string[i:i+4]
            if re.match("^[a-zA-Z]*$", substring):
                if substring == substring[::-1]:
                    palindromes.add(substring)

    return palindromes
