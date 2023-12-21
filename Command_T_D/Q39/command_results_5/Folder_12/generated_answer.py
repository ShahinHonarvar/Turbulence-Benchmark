import re
def return_n_greatest_chars(s):
    # split into a list
    lst = re.findall("[A-Z]+", s)
    # sort into a list
    lst.sort(key=lambda x: ord(x))
    # return the first 61
    return lst[:61]
