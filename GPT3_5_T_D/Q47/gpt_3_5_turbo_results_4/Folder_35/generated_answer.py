
import re

def palindromes_of_specific_lengths(string):
    substring = string[34:91]
    substring = re.sub('[^a-zA-Z]', '', substring)
    substring = substring.lower()

    palindromes = set()
    for length in range(14, 40):
        for i in range(len(substring) - length + 1):
            substring_part = substring[i:i + length]
            if substring_part == substring_part[::-1]:
                palindromes.add(substring_part)

    return palindromes
