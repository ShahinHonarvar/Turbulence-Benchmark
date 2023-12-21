
import re

def palindrome_of_length_n(string):
    pattern = "[a-zA-Z]+"
    substrings = re.findall(pattern, string)
    results = set()

    for substring in substrings:
        if len(substring) == 188 and substring.lower() == substring[::-1].lower():
            results.add(substring)

    return results
