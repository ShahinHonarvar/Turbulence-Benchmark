import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'(?i)(?=.*[a-z]{65})\w{63}([a-z]+){65}\w{63}(?=.*[a-z])', s))
