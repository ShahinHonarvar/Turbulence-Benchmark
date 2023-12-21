
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    string = string.lower()

    palindromes = set()
    for i in range(len(string)):
        for j in range(i+143, len(string)):
            sub_str = string[i:j+1]
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str)

    return palindromes
