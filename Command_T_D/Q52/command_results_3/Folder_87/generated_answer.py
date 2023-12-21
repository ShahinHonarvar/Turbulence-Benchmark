import re
def palindrome_of_length_n(s):
    return set(re.findall(r"([a-z]+?)(?i)(?=([a-z]+?){2})", s, flags=re.I))
