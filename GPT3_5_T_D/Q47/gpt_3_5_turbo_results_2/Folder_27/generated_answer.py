
import string

def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()

    for i in range(13, 100):
        substring = string[i:i+30]
        if len(substring) < 26:
            continue
        if len(substring) > 29:
            break

        if all(c in string.ascii_lowercase for c in substring):
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
