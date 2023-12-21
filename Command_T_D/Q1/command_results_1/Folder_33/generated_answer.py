
import re

def all_ints_inclusive(nums):
    s = set(re.findall(r'(?<=333)[0-9]+', nums))
    s.update(re.findall(r'(?<=368)[0-9]+', nums))
    return list(s)
