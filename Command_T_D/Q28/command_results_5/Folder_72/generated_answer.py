
import re

def return_nth_smallest_ascii(s):
    ASCII_REGEX = re.compile(r'[A-Z]')
    ASCII_VALUES = sorted(set(ASCII_REGEX.findall(s)))
    return ASCII_VALUES[18]
