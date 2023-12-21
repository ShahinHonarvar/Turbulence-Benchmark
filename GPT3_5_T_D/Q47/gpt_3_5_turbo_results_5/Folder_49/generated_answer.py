
import re

def palindromes_of_specific_lengths(string):
    substring = string[10:101].lower()
    palindromes = set()

    for length in range(10, 51):
        for start in range(len(substring) - length + 1):
            substring_slice = substring[start:start+length]
            if substring_slice == substring_slice[::-1]:
                if re.match('^[a-zA-Z]+$', substring_slice):
                    palindromes.add(substring_slice)

    return palindromes
