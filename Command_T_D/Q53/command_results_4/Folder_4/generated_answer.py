import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'(?=([a-z]+){99})([a-z]+)', s.lower()))
