def return_n_smallest_chars(str_list):
    res = []
    for c in str_list:
        if ord(c) < max(res) and ord(c) > min(res):
            res.append(c)
    return res
