import re
def palindrome_of_length_at_least_n(s):
    if s:
        return re.findall(r'[a-z]+\Z', s, flags=re.I)
    else:
        return set()
