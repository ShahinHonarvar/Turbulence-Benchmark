import re
def palindrome_of_length_n(s):
    return set(re.findall(r'[a-z]+\Z', s.lower(), flags=re.I))
