def find_original_set(s):
    lst = set(s)
    for i in range(len(lst)):
        if lst:
            lst -= s.pop()
            s.add(lst)
    return s
