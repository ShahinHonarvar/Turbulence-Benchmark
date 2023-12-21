import re
def palindrome_of_length_at_least_n(s):
    m = re.findall(r'(?=.)(.)\1', s.lower())
    return set(m if len(m) > 0 else set())
