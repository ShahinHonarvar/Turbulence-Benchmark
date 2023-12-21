def palindrome_of_length_at_least_n(s):
    import re
    return set(re.findall(r'[A-Z]+[A-Z]+[A-Z]+', s.lower()))
