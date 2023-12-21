import re
def palindrome_of_length_n(s):
    return set(re.findall(r'[a-z]{49}|([a-z]{2}){47}([a-z]{2})', s.lower()))
