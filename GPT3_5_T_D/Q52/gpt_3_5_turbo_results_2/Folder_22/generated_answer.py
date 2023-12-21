
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    pattern = re.compile(r'[a-zA-Z]+')

    for i in range(len(string) - 19):
        substring = string[i:i+20]
        if len(pattern.findall(substring)) > 0 and substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
