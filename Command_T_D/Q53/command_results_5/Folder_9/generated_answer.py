import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'[a-z]{1,95}(\b[a-z]{1,95})', s.lower()))
