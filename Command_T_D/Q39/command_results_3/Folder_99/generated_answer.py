import re
def return_n_greatest_chars(s):
    m = re.findall("[a-z]", s)
    return m[:35]
