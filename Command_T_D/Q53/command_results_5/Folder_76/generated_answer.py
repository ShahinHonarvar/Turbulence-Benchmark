import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'[a-z]{0,}\w{0,}{0,}'.lower(), s))
