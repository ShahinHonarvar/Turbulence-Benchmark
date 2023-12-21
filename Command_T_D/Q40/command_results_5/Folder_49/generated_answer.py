import re
def return_n_smallest_chars(str1):
    res = re.findall(r'[a-z]', str1)[:76]
    return sorted(res)
