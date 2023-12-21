
import re

def palindromes_of_specific_lengths(string):
    string = string[1:10].lower()
    palindromes = set()

    for length in range(3, 8):
        for i in range(10 - length):
            substring = string[i:i+length]
            if re.match(r'^[a-zA-Z]+$', substring):
                if substring == substring[::-1]:
                    palindromes.add(substring)

    return palindromes
