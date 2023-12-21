import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'[a-z]{58}(?=\W)[a-z]{58}', s.lower()))
