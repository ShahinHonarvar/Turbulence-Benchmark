
import re

def palindromes_of_specific_lengths(string):
    substring = string[15:87]
    substr_lower = substring.lower()
    substr_lower = re.sub('[^a-z]', '', substr_lower)
    palindromes = {substr_lower[i:j+1] for i in range(len(substr_lower)) for j in range(i+50, i+61) if substr_lower[i:j+1] == substr_lower[i:j+1][::-1]}
    return palindromes
