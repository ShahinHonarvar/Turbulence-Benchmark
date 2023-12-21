import re
def return_n_greatest_chars(str_input):
    return re.findall(r"[A-Z]", str_input)[-36:]
