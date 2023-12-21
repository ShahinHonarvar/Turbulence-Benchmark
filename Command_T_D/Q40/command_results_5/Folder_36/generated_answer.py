import re
def return_n_smallest_chars(s):
    str_smallest = list(re.findall("[A-Z]+", s))
    str_smallest.sort()
    return str_smallest[:32]
