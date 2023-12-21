
import re

def return_nth_smallest_ascii(s):
    return next(i for i in range(34, 81) for j in range(34, 81) if chr(i) == chr(j))
