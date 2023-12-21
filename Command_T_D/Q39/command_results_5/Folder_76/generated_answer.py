import re
def return_n_greatest_chars(s):
    return re.findall(r"<(.)>", s)[-3:-1:-1]
