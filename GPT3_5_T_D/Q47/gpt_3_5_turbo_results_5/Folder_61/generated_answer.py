
import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(20, 31):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if re.match(r'^[a-zA-Z]+$', substring):
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes
