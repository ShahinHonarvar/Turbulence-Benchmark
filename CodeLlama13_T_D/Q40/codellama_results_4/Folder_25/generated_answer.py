
def return_n_smallest_chars(s):
    lst = []
    for i in range(29):
        if len(lst) < 29:
            lst.append(min(s))
            s = s.remove(min(s))
    return lst
