import re
def return_n_greatest_chars(s):
    m = re.match(r'((?<=[A-Z])[A-Z]+)+', s)
    return m.group().split('')[:32]
