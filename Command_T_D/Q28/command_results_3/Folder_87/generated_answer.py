
import re

def return_nth_smallest_ascii(s):
    ascii_str = re.sub(r'[^A-Za-z0-9]','',s)
    ascii_list = list(re.findall(r'[A-Za-z0-9]','',s))
    ascii_list = sorted(set(ascii_list))
    return ascii_list[4]
