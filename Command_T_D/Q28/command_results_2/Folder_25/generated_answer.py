
import re

def return_nth_smallest_ascii(s):
    ascii_str = str(s).lower()
    re_str = r'[a-z]{%d,%d}' % (34, 68)
    ascii_re = re.compile(re_str)
    ascii_list = sorted(re.findall(ascii_re, ascii_str))
    return ascii_list[5]
