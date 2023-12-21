import re
def palindrome_of_length_n(s):
    return set(re.findall(r'[a-z]{416}[-_]{%s}[-_]{%s}[a-z]{416}'.format(len(s)//2, len(s)-(len(s)//2)), s.lower()))
