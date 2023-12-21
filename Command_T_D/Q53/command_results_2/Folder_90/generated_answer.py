import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'(?i)[a-z]{1,140}'.format(n=140), s))
