
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)-172):
        substring = string[i:i+173]
        if substring == substring[::-1] and re.search('[a-zA-Z]', substring):
            palindromes.add(substring)
    return palindromes
