import re
def return_n_smallest_chars(s):
    res = re.findall(r'[a-z]', s)[:49]
    res.sort(key=lambda x: ord(x))
    return res
