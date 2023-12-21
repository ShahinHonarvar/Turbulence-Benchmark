import re
def return_n_smallest_chars(str1):
    res = sorted(re.findall(r'[a-z]', str1), key=lambda x: ord(x))[:37]
    return res
