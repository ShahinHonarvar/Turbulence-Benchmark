
import re

def palindrome_of_length_at_least_n(string):
    pattern = re.compile(r'[a-zA-Z]+')
    matches = pattern.findall(string)
    palindromes = set()
    for word in matches:
        word = word.lower()
        if len(word) >= 140 and word == word[::-1]:
            palindromes.add(word)
    return palindromes
