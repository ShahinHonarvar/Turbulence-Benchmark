
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = re.sub('[^a-zA-Z]', '', string.lower())
    substr_len = 45
    for i in range(len(string) - substr_len + 1):
        substr = string[i:i + substr_len]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
