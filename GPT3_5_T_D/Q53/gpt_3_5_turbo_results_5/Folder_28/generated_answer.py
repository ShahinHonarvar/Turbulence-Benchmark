
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+42, len(string)+1):
            sub_str = string[i:j]
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
    return palindromes
