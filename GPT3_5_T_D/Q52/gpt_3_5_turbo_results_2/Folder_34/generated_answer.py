
import re

def palindrome_of_length_n(string):
    palindromes = set()
    length = 33
    string = re.sub('[^a-zA-Z]', '', string.lower())
    for i in range(len(string) - length + 1):
        substr = string[i:i+length]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
