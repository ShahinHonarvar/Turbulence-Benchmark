import re
def return_n_greatest_chars(str):
    return re.findall("[A-Z]", str)[-64:]
