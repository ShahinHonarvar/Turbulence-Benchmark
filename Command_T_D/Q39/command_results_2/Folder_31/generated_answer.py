import re
def return_n_greatest_chars(str):
    re_str = r'<\w+>'
    m = re.finditer(re_str, str)
    str_list = [w.group() for w in m]
    return sorted(str_list[:70], key=lambda s: ord(s))
