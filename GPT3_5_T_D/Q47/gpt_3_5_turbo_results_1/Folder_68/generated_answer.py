
import re

def palindromes_of_specific_lengths(string):
    substring = string[:51].lower()
    palindromes = set()

    for length in range(50, 101):
        for i in range(len(substring) - length + 1):
            if re.match(r'^[a-zA-Z]+$', substring[i:i+length]):
                if substring[i:i+length] == substring[i:i+length][::-1]:
                    palindromes.add(substring[i:i+length])

    return palindromes
