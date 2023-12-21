
import string

def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for i in range(16, 78):
        substring = string[i:i+47]
        if len(substring) < 43:
            continue
        if all(char in string.ascii_letters for char in substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
