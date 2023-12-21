
import re

def palindromes_of_specific_lengths(string):
    substring = string[125:284]
    substr_lowercase = substring.lower()
    substr_lowercase = re.sub(r'[^a-z]', '', substr_lowercase)
    palindromes = set()
    for length in range(109, 127):
        for i in range(len(substr_lowercase) - length + 1):
            substr = substr_lowercase[i:i+length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
