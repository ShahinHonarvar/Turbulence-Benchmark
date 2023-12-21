
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindrome_set = set()
    for i in range(len(string) - 39):
        substring = string[i:i+40]
        if re.match("^[a-z]*$", substring):
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
