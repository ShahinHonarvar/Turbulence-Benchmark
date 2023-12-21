
import re

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 288):
        substring = string[i:i+289]
        substring = re.sub("[^a-zA-Z]+", "", substring)
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes
