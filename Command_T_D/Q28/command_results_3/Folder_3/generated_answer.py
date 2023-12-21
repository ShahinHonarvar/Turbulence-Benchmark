
import re

def return_nth_smallest_ascii(s):
    i = re.findall(r'[A-Z]', s)[25:45]
    return sorted(i)[10]
