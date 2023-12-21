
import re

def palindrome_of_length_n(string):
    palindrome_set = set()
    string = string.lower()
    for i in range(len(string)-6):
        substring = string[i:i+7]
        if re.match("^[a-zA-Z]+$", substring):
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
