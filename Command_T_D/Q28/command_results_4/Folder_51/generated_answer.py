
import re

def return_nth_smallest_ascii(str):
    ascii_str = re.sub(r'[^A-Z0-9]','',str)
    return str[10:73][-9]
