import re
def return_n_smallest_chars(str):
    return re.findall(r"[a-z]", str)[:32]
