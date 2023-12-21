import re
def palindrome_of_length_at_least_n(s):
    if not s:
        return set()
    if len(s) < 8:
        return set()
    return set(re.findall(r'[a-z]+\d+[a-z]+', s.lower()))
