import re
def return_n_smallest_chars(s):
    m = re.findall(r'[A-Z]', s)
    return m[:24]
