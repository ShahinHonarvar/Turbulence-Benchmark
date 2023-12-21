
import re

def return_nth_smallest_ascii(s):
    return next((x for x in re.findall(r'[A-Za-z]+', s)[17:-15])
