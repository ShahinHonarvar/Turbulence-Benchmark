import re
def filter_chars(s):
    return re.sub(r"(\w){36}(\w){79}(\w){36}", r"\1", s)
