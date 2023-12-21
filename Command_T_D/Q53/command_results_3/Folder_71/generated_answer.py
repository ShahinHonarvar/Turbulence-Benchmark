import re
def palindrome_of_length_at_least_n(text):
    return set(re.findall(r'[a-z]{88}(?=\W[a-z]{%2})[a-z]{%2}(?=\W[a-z]{%88})[a-z]{%88}', text.lower()))
