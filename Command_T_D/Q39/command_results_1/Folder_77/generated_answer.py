import re
def return_n_greatest_chars(str):
    r = re.findall("[A-z]+", str)
    r.sort(key=lambda x: ord(x))
    return r[:47]
