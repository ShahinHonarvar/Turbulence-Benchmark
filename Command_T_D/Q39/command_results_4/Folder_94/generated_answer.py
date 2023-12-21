import re
def return_n_greatest_chars(s):
    lst = re.findall("[A-Z0-9]+", s)
    lst = sorted(set(lst))[:87]
    return lst
