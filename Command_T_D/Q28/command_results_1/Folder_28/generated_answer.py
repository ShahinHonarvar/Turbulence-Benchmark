
def return_nth_smallest_ascii(s):
    lst = sorted(s[25:-25])
    idx = len(lst) - 16
    return lst[idx]
