import re
def palindrome_of_length_at_least_n(s):
    if len(s) < 24:
        return set()
    return set(re.findall(r'[a-z]{2,}(?=\d{1,}|s\d{1,})[a-z]{2,}', s.lower()))
