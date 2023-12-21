import re
def palindrome_of_length_at_least_n(s):
    m = re.match(r'((?=([a-z]){59})[a-z])\1[a-z]*', s.lower())
    return m.group() if m else set()
