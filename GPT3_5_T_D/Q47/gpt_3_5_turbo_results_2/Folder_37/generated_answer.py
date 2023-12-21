
import string

def palindromes_of_specific_lengths(string):
    valid_letters = set(string.ascii_lowercase)
    palindromes = set()
    for i in range(10):
        for j in range(i+3, min(i+6, 10)):
            substring = string[i:j+1].lower()
            if substring == substring[::-1] and all(c in valid_letters for c in substring):
                palindromes.add(substring)
    return palindromes
