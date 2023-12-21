
import re

def palindromes_of_specific_lengths(string):
    substring = string[15:96].lower()
    palindromes = set()

    for i in range(20, 67):
        for j in range(len(substring) - i + 1):
            if re.match(r'^[a-zA-Z]+$', substring[j:j+i]):
                if substring[j:j+i] == substring[j:j+i][::-1]:
                    palindromes.add(substring[j:j+i])

    return palindromes
