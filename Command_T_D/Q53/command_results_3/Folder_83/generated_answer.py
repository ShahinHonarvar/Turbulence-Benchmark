import re
def palindrome_of_length_at_least_n(s):
    m = re.findall(r"<(.*?)>", s)
    if len(m) == 0:
        return set()
    return set(m)
