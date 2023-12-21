import re
def return_n_greatest_chars(s):
    r = re.findall(r'[A-Z]', s)
    return r[:37]
