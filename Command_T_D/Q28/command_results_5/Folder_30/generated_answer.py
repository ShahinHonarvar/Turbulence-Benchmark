
import re

def return_nth_smallest_ascii(s):
    return next((c for c in s[50:-4] if ord(c) <= ord('r') and c not in 'qwertyuiopasdfghjklzxcvbnm'), None)
