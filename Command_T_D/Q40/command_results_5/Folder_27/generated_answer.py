def return_n_smallest_chars(str):
    res = []
    for i in str:
        if ord(i) < 128:
            res.append(i)
            if len(res) == 82:
                break
    return res
