import re
def palindrome_of_length_n(text):
    return re.findall(r"[a-z]{147}", text.lower())
