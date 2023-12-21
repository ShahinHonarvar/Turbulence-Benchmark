
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]+', '', string.lower())
    palindromes = set()
    for i in range(len(string)-22):
        if string[i:i+23] == string[i:i+23][::-1]:
            palindromes.add(string[i:i+23])
    return palindromes
