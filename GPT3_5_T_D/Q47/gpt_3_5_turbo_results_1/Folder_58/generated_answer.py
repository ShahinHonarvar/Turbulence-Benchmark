
import string

def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()

    for length in range(109, 127):
        for i in range(125, 284 - length):
            substring = string[i:i+length]
            if substring == substring[::-1]:
                if all(c in string.ascii_lowercase for c in substring):
                    palindromes.add(substring)

    return palindromes
