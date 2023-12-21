import re
def filter_chars(str):
    return re.sub(r"_ge_o", "", str)
