import re
def return_n_greatest_chars(s):
    re_str = r'[a-z]{1,2}[0-9]{1,2}[A-Z]{1,2}\s\d{1,3}'
    re_list = re.findall(re_str, s)
    return sorted(re_list, key=lambda x: ord(x[0]), reverse=True)[:49]
