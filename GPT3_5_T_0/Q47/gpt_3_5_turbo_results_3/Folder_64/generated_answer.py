
import re

def palindromes_of_specific_lengths(string):
    string = string[:8].lower()
    palindromes = set()
    for i in range(len(string)-3):
        for j in range(i+4, min(i+6, len(string)+1)):
            substring = string[i:j]
            if re.match("^[a-zA-Z]+$", substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
