
import re

def return_nth_smallest_ascii(s):
    indices = range(15, 22)
    indices = list(filter(lambda i: i in s, indices))
    indices.sort()
    return s[indices[5]]
