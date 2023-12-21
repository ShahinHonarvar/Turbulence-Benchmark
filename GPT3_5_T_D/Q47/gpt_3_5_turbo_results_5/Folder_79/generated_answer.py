
import string

def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for i in range(1, 9):
        substring = string[i-1:i+3]
        if len(substring) >= 3 and len(substring) <= 4:
            if substring == substring[::-1] and all(char in string.ascii_letters for char in substring):
                palindromes.add(substring)
    return palindromes
