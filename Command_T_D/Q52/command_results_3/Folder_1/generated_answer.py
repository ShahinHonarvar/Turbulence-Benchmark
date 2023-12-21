import re
def palindrome_of_length_n(s):
    return set(re.findall(r'([a-z]+)(?=\W[a-z]{%d})\1' % (len(s)), s.lower()))
