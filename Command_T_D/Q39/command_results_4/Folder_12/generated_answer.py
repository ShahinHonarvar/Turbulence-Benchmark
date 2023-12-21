import re
def return_n_greatest_chars(str):
    return re.findall(r"[A-Z]", str)[-61:]
