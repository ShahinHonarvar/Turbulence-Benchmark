def palindrome_of_length_at_least_n(s):
    import re
    return set(re.findall(r'(?i)(?=([a-z]){76}(?i))([a-z]){76}(?i))', s))
