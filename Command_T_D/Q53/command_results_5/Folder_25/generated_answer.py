import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'([a-z]+)[a-z]+\1', s.lower()))
