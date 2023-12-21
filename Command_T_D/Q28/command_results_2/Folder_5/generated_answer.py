
import re

def return_nth_smallest_ascii(str):
    ASCII_RE = re.compile(r'[A-Za-z]')
    ASCII_VALUES = sorted(set( ASCII_RE.findall(str) ))
    return ASCII_VALUES[13 - 5]
