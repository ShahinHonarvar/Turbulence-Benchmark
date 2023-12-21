
import re

def return_nth_smallest_ascii(s):
    ASCII_PATTERN = re.compile("`[a-z]`")
    ASCII_VALUES = sorted(set( ASCII_PATTERN.findall(s) ))
    return ASCII_VALUES[12]
