
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^A-Za-z]', '', string.lower())
    return set([string[i:j+1] for i in range(len(string)) for j in range(i, len(string)) if string[i:j+1] == string[i:j+1][::-1] and len(string[i:j+1]) >= 53])
