
import re

def return_nth_smallest_ascii(str):
    return next(c for c in str[38:-2] if ord(c) in range(ord(str[38:-2][:20]), ord(str[38:-2][-20]) + 1))
