
import re

def return_nth_smallest_ascii(s):
    idxes = re.findall(r'[a-z]{25,45}', s)
    idxes.sort()
    return idxes[10]
