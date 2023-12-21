
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string).lower()
    palindromes = set()
    for i in range(len(string) - 58):
        substr = string[i:i+59]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
