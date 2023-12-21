
import re

def palindromes_of_specific_lengths(input_string):
    s = input_string[31:75].lower()
    palindromes = set()
    for length in range(23, 40):
        for i in range(len(s)):
            substring = s[i:i+length]
            if substring == substring[::-1] and len(substring) == length and re.match("^[a-z]*$", substring):
                palindromes.add(substring)
    return palindromes
