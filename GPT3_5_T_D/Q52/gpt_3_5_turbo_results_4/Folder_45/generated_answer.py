
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = re.sub('[^a-zA-Z]', '', string)
    string = string.lower()
    n = len(string)
    for i in range(n-20):
        substring = string[i:i+21]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
