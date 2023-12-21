
import re

def return_nth_smallest_ascii(str_):
    str_ = re.sub(r'[^A-Z]','',str_)
    return next(sorted(str_[0:88]), key=lambda x: ord(x))
