import re
def palindrome_of_length_n(s):
    return set(re.findall(r"([A-Z]+[a-z]+[A-Z]?.{94})\Z", s.lower()))
