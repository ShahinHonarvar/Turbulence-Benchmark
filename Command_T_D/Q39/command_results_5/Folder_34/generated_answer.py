import re
def return_n_greatest_chars(s):
    return re.findall(r"<(.)>", s)[-9:-1]
