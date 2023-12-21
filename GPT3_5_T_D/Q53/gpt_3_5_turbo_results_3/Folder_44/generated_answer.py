
import re

def palindrome_of_length_at_least_n(string: str) -> set:
    palindromes = set()
    
    # Remove non-alphabetic characters and convert to lowercase
    string = re.sub("[^a-zA-Z]", "", string.lower())

    # Iterate through all possible substrings
    for i in range(len(string)):
        for j in range(i + 89, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
