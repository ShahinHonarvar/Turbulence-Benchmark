
import re

def palindrome_of_length_n(string):
    palindromes = []
    string = string.lower()
    for i in range(len(string) - 49):
        sub_string = string[i: i + 50]
        if re.match(r"^[a-zA-Z]+$", sub_string):
            if sub_string == sub_string[::-1]:
                palindromes.append(sub_string)
    return set(palindromes)
