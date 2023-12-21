
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    result = set()
    for i in range(len(string) - 146):
        substring = string[i:i+147]
        if substring == substring[::-1]:
            result.add(substring)
    return result
