import re
def return_n_greatest_chars(str_):
    str_ = re.sub(r'[^A-Z0-9]+', '', str_)
    str_ = str_.upper()
    return str_[0:12]
