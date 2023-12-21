
import re

def palindrome_of_length_n(string):
    string = re.sub('[^A-Za-z]', '', string.lower())
    palindromes = set()
    n = 85
    for i in range(len(string) - n + 1):
        if string[i:i+n] == string[i:i+n][::-1]:
            palindromes.add(string[i:i+n])
    return palindromes
