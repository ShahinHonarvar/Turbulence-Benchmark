import re
def return_n_smallest_chars(str):
    res = re.findall(r'[A-Z]', str)
    res = sorted(set(res))[:52]
    return res
