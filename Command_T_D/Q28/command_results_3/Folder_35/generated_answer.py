
import re

def return_nth_smallest_ascii(s):
    m = re.match(r'<[A-Z]+>'.format(7), s)
    return m.group()
