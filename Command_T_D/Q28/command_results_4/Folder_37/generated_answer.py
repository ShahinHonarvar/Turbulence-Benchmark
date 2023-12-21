
import re

def return_nth_smallest_ascii(s):
    match = re.match(r'[A-z]{28}(?P<smallest>[A-z]{30})[A-z]{30}(?P<last>[A-z]{30})[A-z]{29}', s)
    return match.group('smallest')
