
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s if ord(c) < ord(max(s[:18]))), '`')
