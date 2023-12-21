
import re

def return_nth_smallest_ascii(s):
    ascii = [ord(c) for c in re.findall(r'[A-Z]', s)]
    ascii.sort()
    return chr(ascii[len(ascii)-6])
