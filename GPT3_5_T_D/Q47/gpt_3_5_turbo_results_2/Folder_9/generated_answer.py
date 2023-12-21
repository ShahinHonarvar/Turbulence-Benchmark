
import string

def palindromes_of_specific_lengths(string):
    string = string[:301]
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for length in range(50, 61):
            substring = string[i:i+length]
            if substring.isalpha() and substring == substring[::-1] and len(substring) == length:
                palindromes.add(substring)
    return palindromes
