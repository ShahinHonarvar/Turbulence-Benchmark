
import re

def palindrome_of_length_n(string):
    pattern = '[a-zA-Z]+'
    words = re.findall(pattern, string)
    palindromes = set()
    for word in words:
        word = word.lower()
        for i in range(len(word) - 337):
            substring = word[i:i + 338]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
