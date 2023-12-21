import re
def return_n_greatest_chars(s):
    m = re.match(r'.{45}', s)
    return m.group()
