import re
def palindrome_of_length_at_least_n(text):
    return set(re.findall(r'(?i)(?=([a-z]+[a-z][a-z]+){2,}$)'.format(n=20), text))
