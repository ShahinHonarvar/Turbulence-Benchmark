
def return_nth_smallest_ascii(s):
    lst = sorted(s)
    idx = len(lst) - 16
    return lst[idx - 1]
