
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = []
    for i in range(len(string)-72):
        substring = string[i:i+73]
        if re.match("^[a-zA-Z]+$", substring) and substring == substring[::-1]:
            palindromes.append(substring)
    return set(palindromes)
