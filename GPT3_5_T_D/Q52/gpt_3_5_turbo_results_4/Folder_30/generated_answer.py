
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)-93):
        sub_str = string[i:i+94]
        if re.match(r'^[a-z]+$', sub_str):
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
    return palindromes
