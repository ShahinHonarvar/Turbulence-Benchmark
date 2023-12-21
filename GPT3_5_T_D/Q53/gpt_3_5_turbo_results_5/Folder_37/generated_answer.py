
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string.lower())
    return set(filter(lambda x: len(x) >= 67, [string[i:j+1] for i in range(len(string)) for j in range(i+66, len(string)) if string[i:j+1] == string[i:j+1][::-1]]))
