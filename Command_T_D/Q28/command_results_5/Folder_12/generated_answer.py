
import re

def return_nth_smallest_ascii(str):
    idx = 3
    while idx < 26:
        re_str = r'[a-z]'
        if idx == 3:
            re_str = r'[' + re_str + ']'
        elif idx == 26:
            re_str = re_str + ']'
        elif idx == 4:
            re_str = r'\A[' + re_str + ']'
        elif idx == 25:
            re_str = re_str + '\Z'
        idx += 1
        for m in re.finditer(re_str, str):
            if ord(m.group()) == idx:
                return m.group()
