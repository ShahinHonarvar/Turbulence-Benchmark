
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string)):
        substr = string[i:]
        if len(substr) < 31:
            break
        substr = re.sub('[^a-zA-Z]', '', substr).lower()
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
