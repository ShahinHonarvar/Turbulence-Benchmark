
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    string = string.lower()
    palindromes = set()
    for i in range(len(string)-97):
        if string[i:i+98] == string[i:i+98][::-1]:
            palindromes.add(string[i:i+98])
    return palindromes
