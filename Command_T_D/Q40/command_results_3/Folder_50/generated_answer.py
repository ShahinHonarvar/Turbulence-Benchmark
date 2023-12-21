import re
def return_n_smallest_chars(s):
    return re.findall(r"<(.)>", s)[0][1:-1]
