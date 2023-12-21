
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 38):
        if re.match("^[a-zA-Z]+$", string[i:i+39]) and string[i:i+39] == string[i:i+39][::-1]:
            palindromes.add(string[i:i+39])
    return palindromes
