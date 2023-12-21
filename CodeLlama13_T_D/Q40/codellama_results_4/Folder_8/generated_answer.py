
def return_n_smallest_chars(s):
    lst = []
    for i in range(83):
        lst.append(min(s, key=ord))
        s.remove(lst[-1])
    return sorted(lst)
