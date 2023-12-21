import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'(?i)[a-z]+[a-z]+'.format(n=147), s))
