import re
def palindrome_of_length_at_least_n(s):
    if len(s) < 3:
        return set()
    else:
        return set(re.findall(r'(?i)(?=([a-z]{2,}(?:[a-z])))', s))
