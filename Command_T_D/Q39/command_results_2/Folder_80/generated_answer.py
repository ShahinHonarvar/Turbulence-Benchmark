def return_n_greatest_chars(str):
    res = []
    for i in str:
        res.append(i)
    res.sort()
    res = res[:35]
    return res
