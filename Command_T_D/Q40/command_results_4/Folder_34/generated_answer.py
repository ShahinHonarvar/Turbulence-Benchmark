import re
def return_n_smallest_chars(s):
    m = re.findall(r'(.)', s)
    return m[:9]
