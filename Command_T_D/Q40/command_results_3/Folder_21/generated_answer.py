def return_n_smallest_chars(s):
    lst = []
    for i in range(len(s)):
        if s[i] not in lst:
            lst.append(s[i])
            if len(lst) == 44:
                break
    return lst
