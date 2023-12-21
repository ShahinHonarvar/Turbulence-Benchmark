import re
def return_n_greatest_chars(str1):
    res = re.findall(r'\w+', str1)[:17]
    return sorted(set(res))
