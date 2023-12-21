
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    palindrome_set = set()
    substring_length = 255

    for i in range(len(string) - substring_length + 1):
        substring = string[i:i + substring_length]
        if substring == substring[::-1]:
            palindrome_set.add(substring)

    return palindrome_set
