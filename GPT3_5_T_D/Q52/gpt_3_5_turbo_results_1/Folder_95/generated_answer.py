
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string)  # removing any non-English letters
    palindromes = set()
    n = 87
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        if substr.lower() == substr.lower()[::-1]:
            palindromes.add(substr)
    return palindromes
