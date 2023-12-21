import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'[a-z]{38}([a-z]{35})[a-z]{2}([a-z]{35})[a-z]{38}', s.lower()))
