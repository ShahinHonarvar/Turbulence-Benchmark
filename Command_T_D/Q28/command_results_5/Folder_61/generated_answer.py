
import re

def return_nth_smallest_ascii(s):
    idx = 0
    while idx < 10:
        idx += 1
        if idx >= len(s):
            break
        char = s[idx - 1]
        if char.isalpha():
            idx -= 1
            break
    idx -= 1
    ascii = ord(s[idx])
    return s[idx]
