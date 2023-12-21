
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()

    for i in range(len(string)):
        for j in range(i + 138, len(string) + 1):
            substring = string[i:j]
            if re.match('^[a-zA-Z]+$', substring):
                reversed_substring = substring[::-1]
                if substring == reversed_substring:
                    palindromes.add(substring)

    return palindromes
