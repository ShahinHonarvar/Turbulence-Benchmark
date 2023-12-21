import re
def return_n_greatest_chars(s):
    m = re.match(r'(\S+)', s)
    return m.group().split('')[:35]
