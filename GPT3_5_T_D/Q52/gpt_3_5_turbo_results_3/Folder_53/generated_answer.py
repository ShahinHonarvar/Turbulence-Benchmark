
import re

def palindrome_of_length_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    string = string.lower()

    palindromes = set()
    n = 68

    for i in range(len(string) - n + 1):
        sub_string = string[i:i+n]
        if sub_string == sub_string[::-1]:
            palindromes.add(sub_string)

    return palindromes
