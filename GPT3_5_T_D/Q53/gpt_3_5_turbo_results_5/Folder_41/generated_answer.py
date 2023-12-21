
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub("[^a-zA-Z]+", "", string).lower()
    palindromes = set()
    for i in range(len(string)-27):
        for j in range(28, len(string)-i+1):
            substring = string[i:i+j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
