
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub("[^a-zA-Z]", "", string.lower())
    palindromes = set()
    n = len(string)
    for length in range(85, n+1):
        for start in range(n-length+1):
            substring = string[start:start+length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
