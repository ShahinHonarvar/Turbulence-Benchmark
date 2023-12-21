
import re

def palindrome_of_length_n(string):
    palindrome_set = set()
    n = 97
    string = string.lower()
    string = re.sub('[^a-z]', '', string)
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            palindrome_set.add(substring)
    return palindrome_set
