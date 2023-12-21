
import re

def return_nth_smallest_ascii(s):
    indices = list(range(17, 65+1))
    indices = sorted(set(re.findall(r'[a-z]', s)))
    indices = indices[indices.index(indices[8])+1:8:-1]
    return indices[0]
