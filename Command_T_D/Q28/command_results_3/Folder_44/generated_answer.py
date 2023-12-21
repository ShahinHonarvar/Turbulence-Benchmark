
import re

def return_nth_smallest_ascii(str):
    return next(c for c in str[20:30] if ord(c) in (ord(a) for a in str if a[0] in 'qwertyuiopasdfghjklzxcvbnm'))
