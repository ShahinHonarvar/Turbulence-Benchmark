
import string

def palindromes_of_specific_lengths(string):
    string = string.lower()
    string = string[16:61]
    palindromes = set()
    for length in range(16, 40):
        for start in range(len(string) - length + 1):
            substring = string[start:start+length]
            if substring == substring[::-1] and all(char in string.ascii_letters for char in substring):
                palindromes.add(substring)
    return palindromes
