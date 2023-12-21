
import re

def palindromes_of_specific_lengths(string):
    substring = string[:101]

    palindromes = set()
    for length in range(3, 16):
        regex = r'(?i)([a-zA-Z]{%d})' % length
        matches = re.findall(regex, substring)
        for match in matches:
            if match.lower() == match.lower()[::-1]:
                palindromes.add(match)

    return palindromes
