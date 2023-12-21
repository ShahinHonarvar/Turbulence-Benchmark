
import re

def palindromes_of_specific_lengths(string):
    string = string.lower()
    substring = string[1:9]
    palindromes = set()

    for i in range(len(substring)):
        for length in range(3, 5):
            if i + length <= len(substring):
                sub = substring[i:i+length]
                if re.match('^[a-zA-Z]+$', sub):
                    if sub == sub[::-1]:
                        palindromes.add(sub)

    return palindromes
