
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 44):
        if string[i:i+45] == string[i:i+45][::-1] and re.match("^[a-zA-Z]+$", string[i:i+45]):
            palindromes.add(string[i:i+45])
    return palindromes
