import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'(?i)[a-z]{2,}(?i)([a-z]+)', s, flags=re.I))
