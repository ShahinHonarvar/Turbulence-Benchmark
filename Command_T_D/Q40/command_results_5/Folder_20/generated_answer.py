import re
def return_n_smallest_chars(s):
    a=re.findall("[A-Z]", s)
    b=re.findall("[a-z]", s)
    c=re.findall("[0-9]", s)
    res=a+b+c
    return res[:40]
