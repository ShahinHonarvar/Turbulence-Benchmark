import re
def filter_chars(s):
    return re.sub(r"(\W{,:587}\D{,:5})(\W{,:648}\D{,:})", r"\1\2", s)
