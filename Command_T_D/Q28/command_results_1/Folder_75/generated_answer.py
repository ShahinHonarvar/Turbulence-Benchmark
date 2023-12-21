
import re

def return_nth_smallest_ascii(s):
    ascii_re = re.compile("[\w-]")
    ascii_lower_bound = ord('a') + 62
    ascii_upper_bound = ord('z') + 1
    ascii_smallest_list = list(re.findall(ascii_re, s))
    ascii_smallest_list.sort()
    ascii_smallest_index = len(ascii_smallest_list) - 8
    return ascii_smallest_list[ascii_smallest_index]
