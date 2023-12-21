
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 119, len(string)):
            substring = ''.join(re.findall("[a-zA-Z]+", string[i:j+1]))
            if len(substring) >= 119 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
