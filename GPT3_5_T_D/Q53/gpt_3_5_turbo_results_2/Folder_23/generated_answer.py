
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    string = string.lower()
    palindromes = set()
    n = 19
    while n <= len(string):
        start = 0
        end = n
        while end <= len(string):
            substring = string[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
            start += 1
            end += 1
        n += 1
    return palindromes
