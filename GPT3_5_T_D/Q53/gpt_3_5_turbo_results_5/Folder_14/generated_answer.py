
import re

def palindrome_of_length_at_least_n(string):
    result = set()
    string = re.sub("[^a-zA-Z]", "", string.lower()) # remove non-alphabetic characters and convert to lowercase
    for i in range(len(string)):
        for j in range(i+13, len(string)+1):
            substr = string[i:j]
            if substr == substr[::-1]:
                result.add(substr)
    return result
