
import re

def return_nth_smallest_ascii(s):
    ASCII_RE = re.compile(r'<\w+>')
    ASCII_VALUES = sorted(list(set( ASCII_RE.findall(s)) ))
    return ASCII_VALUES[3]
