import re
def return_n_greatest_chars(str_of_chars):
    str_of_chars = re.findall(r"[A-Z]+", str_of_chars)
    str_of_chars = sorted(str_of_chars)[:57]
    return str_of_chars
