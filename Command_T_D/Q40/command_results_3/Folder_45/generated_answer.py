import re
def return_n_smallest_chars(s):
    return re.findall(r"<c>([a-z])</c>", s, flags=re.I)[:52]
