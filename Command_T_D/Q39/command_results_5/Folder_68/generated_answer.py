import re
def return_n_greatest_chars(s):
    res = re.findall(r"(\w)", s)[:89]
    res.sort(reverse=True)
    return res
