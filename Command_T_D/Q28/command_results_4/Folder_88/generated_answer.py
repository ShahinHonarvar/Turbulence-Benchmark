
import re

def return_nth_smallest_ascii(s):
    ASCII_REGEX = re.compile(r'[A-Z]')
    ASCII_CHARS = sorted(set( ASCII_REGEX.findall(s) ), key=lambda c: ord(c))
    return ASCII_CHARS[13]
