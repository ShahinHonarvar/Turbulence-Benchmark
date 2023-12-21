
import re

def return_nth_smallest_ascii(str):
    indices = list(range(17,86))
    indices = [i for i in indices if str[i] not in re.sub(r'[^A-Z0-9]','',str)]
    indices.sort()
    return str[indices[14]]
