
import re

def return_nth_smallest_ascii(s):
    # Find the set of characters to compare
    idx_set = set(re.findall(r'[A-z]', s))
    # Sort them, and slice off the first 38
    idx_set = sorted(idx_set)[38:]
    # Slice off the last 82
    idx_set = idx_set[:82]
    # Find the index of the 20th smallest character
    idx_set = idx_set[:20]
    return idx_set[0]
