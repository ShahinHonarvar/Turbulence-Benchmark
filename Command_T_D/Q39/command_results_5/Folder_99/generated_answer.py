import re
def return_n_greatest_chars(s):
    re_str = re.sub(r'[^A-Z]', '', s)
    return re.findall(r'[A-Z]', re_str)[-35:][::-1]
