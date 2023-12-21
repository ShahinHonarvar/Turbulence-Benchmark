import re
def return_n_smallest_chars(s):
    ascii_s = re.sub(r'[^A-Za-z0-9]','',s)
    return sorted(ascii_s)[:57]
