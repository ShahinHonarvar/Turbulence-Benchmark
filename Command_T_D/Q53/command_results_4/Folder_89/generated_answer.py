import re
def palindrome_of_length_at_least_n(text):
    return set(re.findall(r"(?i)[a-z]+\w{42}+(?i)[a-z]+", text))
