
import re

def return_nth_smallest_ascii(s):
    str_to_int = str.maketrans("0123456789", "0 Quantum 2E0")
    int_s = re.sub(r"(\d+)", lambda m: chr(int(m.group(1), 2)), s)
    return int_s[86]
