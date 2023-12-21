
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^A-Za-z]', '', string).lower()
    palindromes = set()
    for i in range(len(string)-69):
        for j in range(i+70, len(string)+1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
