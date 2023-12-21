
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = re.sub("[^a-zA-Z]", "", string.lower())
    for i in range(len(string)):
        for j in range(i + 41, len(string) + 1):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
