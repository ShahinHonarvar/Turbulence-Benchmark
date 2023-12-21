
import re

def palindrome_of_length_n(string):
    palindromes_set = set()
    string = string.lower()

    for i in range(len(string)):
        for j in range(i+27, len(string)+1):
            substring = string[i:j]
            if re.match('^[a-zA-Z]+$', substring) and substring == substring[::-1]:
                palindromes_set.add(substring)

    return palindromes_set
