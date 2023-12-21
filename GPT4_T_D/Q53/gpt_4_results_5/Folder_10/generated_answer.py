
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string.lower())
    result_set = set()

    for i in range(len(string)):
        for j in range(i + 92, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                result_set.add(substring)

    return result_set
