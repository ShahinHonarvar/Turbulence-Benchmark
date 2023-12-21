
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 62, len(string) + 1):
            substring = string[i:j]
            if re.match(r'^[a-z]+$', substring):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes
