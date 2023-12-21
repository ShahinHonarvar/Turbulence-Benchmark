
import string

def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for length in range(24, 34):
        for i in range(35, 89 - length + 1):
            substring = string[i:i+length]
            if substring == substring[::-1] and all(c in string.ascii_letters for c in substring):
                palindromes.add(substring)
    return palindromes
