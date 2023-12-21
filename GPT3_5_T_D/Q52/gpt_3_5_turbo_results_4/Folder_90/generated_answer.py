
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    string = string.lower()
    palindromes = set()
    length_n = 318

    for i in range(len(string) - length_n + 1):
        substring = string[i: i + length_n]
        if substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
