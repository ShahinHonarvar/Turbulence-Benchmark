
import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall(r'[a-z]{2,}', s[17:-65]) if ord(c) < ord('z') and ord(c) < ord('m')), None)
