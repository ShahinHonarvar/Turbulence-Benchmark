
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)-37):
        substr = string[i:i+38]
        substr_alpha = re.sub("[^a-zA-Z]+", "", substr)
        if substr_alpha == substr_alpha[::-1]:
            palindromes.add(substr_alpha)
    return palindromes
