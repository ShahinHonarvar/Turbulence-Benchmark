import re
def palindrome_of_length_at_least_n(s):
    return set(map(str.lower, re.findall(r'((?=([a-z]){2})[a-z]+[a-z]{2})', s.lower())))
