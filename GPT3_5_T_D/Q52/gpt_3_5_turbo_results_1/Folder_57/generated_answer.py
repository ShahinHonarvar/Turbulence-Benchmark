
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    length = 92
    palindromes = set()
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes
