import re
def palindrome_of_length_n(s):
    return set(re.findall(r'[a-z]{84}|([a-z]{84})\1', s.lower()))
