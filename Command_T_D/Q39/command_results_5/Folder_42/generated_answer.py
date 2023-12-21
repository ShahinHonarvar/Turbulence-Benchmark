import re
def return_n_greatest_chars(s):
    x = re.findall(r'[A-Z]+', s)
    x.sort(key=lambda x: ord(x))
    return x[:59]
