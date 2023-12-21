
import re

def return_nth_smallest_ascii(s):
    m = re.match(r'<([^>]*?)>([a-z]+)', s)
    return next((c for c in m.group(2) if ord(c) in range(ord('c') + 3, ord('z') + 1)), None)
