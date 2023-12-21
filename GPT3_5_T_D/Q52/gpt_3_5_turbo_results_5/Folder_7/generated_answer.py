
import re

def palindrome_of_length_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    n = 416
    palindromes = set()
    for i in range(len(string) - n + 1):
        sub_string = string[i:i+n]
        if sub_string.lower() == sub_string.lower()[::-1]:
            palindromes.add(sub_string)
    return palindromes
