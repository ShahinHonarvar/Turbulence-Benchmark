import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'(?i)(?=([a-z]{|i})[a-z]{|i})' + r'([a-z]{|i})[a-z]{|i})', s))
