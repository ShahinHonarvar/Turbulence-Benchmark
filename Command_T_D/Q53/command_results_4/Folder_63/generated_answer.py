import re
def palindrome_of_length_at_least_n(text):
    return re.findall(r"<(.)?>(?=.)<\1>", text.lower())
