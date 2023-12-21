
import re

def palindrome_of_length_n(string):
    palindromes = set()
    pattern = re.compile('[a-zA-Z]+')
    words = re.findall(pattern, string)
    for word in words:
        if len(word) == 84:
            lowercase_word = word.lower()
            if lowercase_word == lowercase_word[::-1]:
                palindromes.add(word)
    return palindromes
