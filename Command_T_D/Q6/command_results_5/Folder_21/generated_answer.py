import re
def all_neg_ints_exclusive(lst):
    start, stop = str(743), str(867)
    return re.findall(r"-?[0-9]+", lst[start:stop+1])
