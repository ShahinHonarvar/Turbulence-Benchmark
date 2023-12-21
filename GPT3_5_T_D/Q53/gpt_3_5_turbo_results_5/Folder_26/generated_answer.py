
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    normalized_string = re.sub(r'[^a-zA-Z]', '', string.lower())
    for i in range(len(normalized_string)):
        for j in range(i + 32, len(normalized_string) + 1):
            substring = normalized_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
