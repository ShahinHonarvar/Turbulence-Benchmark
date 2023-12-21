
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    length = 56
    palindromes = set()
    for i in range(len(string)-length+1):
        substr = string[i:i+length]
        if substr.lower() == substr.lower()[::-1]:
            palindromes.add(substr)
    return palindromes
