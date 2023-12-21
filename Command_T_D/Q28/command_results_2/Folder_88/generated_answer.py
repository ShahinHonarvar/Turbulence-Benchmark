
import re

def return_nth_smallest_ascii(str):
    start = 38
    end = 64
    return re.findall(r'[A-Z]', str)[start:end+1][13]
