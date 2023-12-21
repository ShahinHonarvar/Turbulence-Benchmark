import re
def return_n_smallest_chars(s):
    m = re.findall(r"(\w)", s)
    return sorted(m[0:23], key=lambda x: ord(x))
