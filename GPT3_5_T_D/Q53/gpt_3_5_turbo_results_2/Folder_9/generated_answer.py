
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+94, len(string)):
            word = string[i:j+1]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
