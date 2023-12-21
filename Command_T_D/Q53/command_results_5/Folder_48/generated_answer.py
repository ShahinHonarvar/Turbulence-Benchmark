import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'[a-z]+\w{149}+[a-z]+\w{149}+', s.lower()))
