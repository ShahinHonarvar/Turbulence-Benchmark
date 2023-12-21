
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+25, len(string)):
            substr = string[i:j+1]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
