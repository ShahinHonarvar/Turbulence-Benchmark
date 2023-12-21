import re
def palindrome_of_length_at_least_n(text):
    if len(text) < 64:
        return set()
    return set(re.findall(r'(?i)[a-z]+', text))
