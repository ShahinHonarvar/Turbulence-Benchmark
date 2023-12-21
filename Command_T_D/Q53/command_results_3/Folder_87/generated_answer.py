import re
def palindrome_of_length_at_least_n(s):
    m = re.findall(r'(?i)[a-z]+'.rstrip('0'), s, flags=re.I)
    return set(m)
