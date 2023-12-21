
import re

def return_nth_smallest_ascii(s):
    if s == "":
        return ""
    else:
        res = list(re.findall(r"[a-z]", s[20:80]))
        res.sort()
        return res[10]
