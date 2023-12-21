
import re

def palindromes_of_specific_lengths(string):
    string = string[:8].lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 4, min(i + 6, len(string) + 1)):
            substring = string[i:j]
            if substring == substring[::-1] and re.match("^[a-zA-Z]+$", substring):
                palindromes.add(substring)
    return palindromes
