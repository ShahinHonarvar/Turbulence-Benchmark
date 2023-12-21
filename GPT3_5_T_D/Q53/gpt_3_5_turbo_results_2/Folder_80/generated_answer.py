
import re

def palindrome_of_length_at_least_n(str):
    pattern = re.compile(r'\b\w{30,}\b', re.IGNORECASE)
    palindromes = set()
    for match in re.findall(pattern, str):
        match = match.lower()
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes
