import re
def return_n_greatest_chars(str1):
    res = re.findall(r'.', str1)[::-1][:28]
    return res
