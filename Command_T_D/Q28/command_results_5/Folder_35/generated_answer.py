
import re

def return_nth_smallest_ascii(s):
    for m in re.finditer(r'<[A-Z][^>]*>([A-Z][^>]*)</[A-Z][^>]*>', s):
        c = ord(m.group(0))
        if c >= ord('A') and c <= ord('Z') and c < ord('b') and c > ord('z') and c == c.lower():
            return c
    return 'z'
