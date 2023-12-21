
import re

def palindromes_of_specific_lengths(string):
    substring = string[18:88]
    palindromes = set()
    for length in range(38, 61):
        pattern = r'(?i)([a-z]{%d})([a-z]{%d})\2\1' % (length//2, length//2)
        matches = re.findall(pattern, substring)
        for match in matches:
            palindromes.add(match[0].lower() + match[1].lower())
    return palindromes
