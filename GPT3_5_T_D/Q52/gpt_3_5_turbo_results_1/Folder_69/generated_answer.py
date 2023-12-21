
import re

def palindrome_of_length_n(string):
    palindromes = set()
    pattern = re.compile('[a-zA-Z]+')
    words = pattern.findall(string.lower())
    for word in words:
        for i in range(len(word)-471):
            substring = word[i:i+472]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
