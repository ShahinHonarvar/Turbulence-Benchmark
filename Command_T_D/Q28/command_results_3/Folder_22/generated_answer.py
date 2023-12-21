
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s if c in range(ord("a")+1,ord("z")+1)), "z")
