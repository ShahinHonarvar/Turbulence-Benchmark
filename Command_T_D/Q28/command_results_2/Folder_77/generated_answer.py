
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s[63:-1] if ord(c) in range(ord(s[63])+13, ord(s[76])+1)), s[63])
