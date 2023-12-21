
import re

def palindromes_of_specific_lengths(string):
    string = string[:11].lower()
    palindromes = set()
    for i in range(len(string)-2):
        for j in range(i+3, min(i+6, len(string)+1)):
            substr = string[i:j]
            if re.match("^[a-zA-Z]+$", substr) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
