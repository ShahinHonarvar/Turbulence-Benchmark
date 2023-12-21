import re
def palindrome_of_length_at_least_n(s):
    if len(s) < 88:
        return set()
    return set(re.findall(r'[a-z]+\d+[a-z]+', s, flags=re.I))
