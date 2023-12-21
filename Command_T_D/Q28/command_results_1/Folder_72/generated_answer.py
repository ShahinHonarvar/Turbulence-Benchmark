
import re

def return_nth_smallest_ascii(s):
    idx = 33
    idx_end = 60
    ascii_val_list = []
    for c in re.findall(r'[A-Z]', s):
        ascii_val_list.append(ord(c))
    ascii_val_list.sort()
    return ascii_val_list[idx]
