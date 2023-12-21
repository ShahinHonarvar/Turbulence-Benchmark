import re
def palindrome_of_length_at_least_n(s):
    return set(re.findall(r"((?i[a-z]+)(?=\s[a-z]{74}(?:\s[a-z]+){74}(?i[a-z]+)))", s))
