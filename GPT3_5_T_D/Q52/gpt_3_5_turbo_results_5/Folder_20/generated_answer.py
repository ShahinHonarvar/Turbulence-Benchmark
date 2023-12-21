
import re

def palindrome_of_length_n(string):
    n = 53
    pattern = r'[A-Za-z]{%d}' % n
    match = re.findall(pattern, string)
    palindromes = set()
    for substring in match:
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes
