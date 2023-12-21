
import re

def return_nth_smallest_ascii(s):
    return re.sub(r'\w', lambda m: str(m.end()), s)[8]
