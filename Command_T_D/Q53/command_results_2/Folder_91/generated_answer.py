import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'(?i)[a-z]{8,}|(?i)[a-z]{7,}\s[a-z]{1})', s))
