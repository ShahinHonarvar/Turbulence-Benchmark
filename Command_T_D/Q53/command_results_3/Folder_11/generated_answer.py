import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r'[a-z]{55,}(?=([a-z]{1}){55,}\1)', s.lower()))
