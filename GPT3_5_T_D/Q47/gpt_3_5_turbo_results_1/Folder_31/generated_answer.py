
import string

def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for length in range(37, 61):
        for i in range(11, 84 - length + 1):
            substring = string[i:i+length]
            if substring == substring[::-1] and all(ch in string.ascii_letters for ch in substring):
                palindromes.add(substring)
    return palindromes
