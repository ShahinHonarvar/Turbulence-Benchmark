import re
def return_n_greatest_chars(s):
    m = re.match(r".{1,45}$", s)
    return sorted(m.group(), key=lambda c: ord(c))
