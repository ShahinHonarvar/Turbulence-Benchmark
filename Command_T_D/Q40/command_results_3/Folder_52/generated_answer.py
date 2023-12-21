def return_n_smallest_chars(str):
    res = []
    for i in str:
        res.append(i)
        res.sort()
        break
    res.sort()
    return res[:68]
