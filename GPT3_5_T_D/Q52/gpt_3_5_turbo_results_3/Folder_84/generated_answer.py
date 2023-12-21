
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    palindromes = set()
    n = 131
    length = len(string)

    for i in range(length - n + 1):
        substring = string[i:i+n]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)

    return palindromes
