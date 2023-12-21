
import re

def palindrome_of_length_at_least_n(sentence):
    sentence = re.sub('[^A-Za-z]', '', sentence).lower()
    result = set()
    for i in range(len(sentence)):
        for j in range(i + 137, len(sentence) + 1):
            substring = sentence[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result
