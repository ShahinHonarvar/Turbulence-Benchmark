
import string

def palindromes_of_specific_lengths(string):
    string = string[:7].lower()
    palindromes = set()
    for length in range(3, 7):
        for start in range(7 - length + 1):
            substring = string[start:start + length]
            if substring == substring[::-1] and all(char in string.ascii_letters for char in substring):
                palindromes.add(substring)
    return palindromes
