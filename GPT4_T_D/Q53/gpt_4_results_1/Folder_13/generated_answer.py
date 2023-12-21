
import re

def palindrome_of_length_at_least_n(input_string):
    input_string = re.sub('[^A-Za-z]', '', input_string).lower()
    palindrome_set = set()
    for i in range(len(input_string)):
        for j in range(i + 52, len(input_string) + 1):
            substring = input_string[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set
