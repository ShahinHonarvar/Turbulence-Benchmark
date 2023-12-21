
import re

def palindrome_of_length_at_least_n(given_string):
    given_string = given_string.lower()
    given_string = re.sub(r'[^a-z]', '', given_string)
    n = 29
    palindromes = set()

    for i in range(0, len(given_string)):
        for j in range(i + n, len(given_string) + 1):
            substring = given_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
                
    return palindromes
