
def all_ints_not_div_by_num(arr):
    res = []
    for i in range(6):
        if arr[i] % 13 != 0:
            res.append(arr[i])
    return res
