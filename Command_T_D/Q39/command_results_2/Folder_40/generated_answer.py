import re
def return_n_greatest_chars(s):
    str_list = re.findall(r'[a-z]', s)
    return sorted(str_list[:7], key=lambda x: ord(x), reverse=True)
