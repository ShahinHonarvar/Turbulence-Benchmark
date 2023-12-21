
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string.lower())
    palindromes = set()
    n = 64
    while n <= len(string):
        for i in range(len(string) - n + 1):
            substring = string[i:i+n]
            if substring == substring[::-1]:
                palindromes.add(substring)
        n += 1
    return palindromes
