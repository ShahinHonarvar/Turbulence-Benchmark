import re
def palindrome_of_length_at_least_n(text):
    if not re.fullmatch(r"<(.*?)>", text):
        return set()
    return set(re.findall(r"<(.*?)>", text))
