
import re

def palindrome_of_length_n(text):
    text = re.sub("[^a-zA-Z]", "", text)
    palindromes = set()
    n = 257
    for i in range(len(text) - n + 1):
        substring = text[i:i + n]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes
