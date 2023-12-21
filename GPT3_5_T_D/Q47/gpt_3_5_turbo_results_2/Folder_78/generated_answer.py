
import re

def palindromes_of_specific_lengths(string):
    substring = string[15:73]
    palindromes = set()

    for length in range(19, 56):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            sub = re.sub('[^a-zA-Z]', '', sub)
            sub = sub.lower()
            if sub == sub[::-1]:
                palindromes.add(sub)

    return palindromes
