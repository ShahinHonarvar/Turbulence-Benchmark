
def return_n_smallest_chars(s):
    lst = []
    for i in range(49):
        lst.append(min(s))
        s.remove(lst[-1])
    return lst
