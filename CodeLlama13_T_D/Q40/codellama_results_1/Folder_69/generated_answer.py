
def return_n_smallest_chars(s):
    lst = []
    for i in range(65):
        if i < len(s):
            lst.append(s[i])
    lst.sort()
    return lst
