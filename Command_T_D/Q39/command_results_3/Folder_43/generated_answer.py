import re
def return_n_greatest_chars(s):
    return sorted(re.findall(r'[a-z]', s)[::-1][:56])
