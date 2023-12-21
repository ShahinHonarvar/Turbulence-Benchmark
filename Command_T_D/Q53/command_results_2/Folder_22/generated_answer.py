def palindrome_of_length_at_least_n(s):
    import re
    return set(re.findall(r'[a-z]+\d{2,}+[a-z]+', s.lower()))
