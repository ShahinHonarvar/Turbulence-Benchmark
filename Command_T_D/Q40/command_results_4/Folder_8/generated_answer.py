import re
def return_n_smallest_chars(s):
    res = re.findall(r"<[a-z]>", s)
    res = sorted(res)
    res = res[:83]
    return res
