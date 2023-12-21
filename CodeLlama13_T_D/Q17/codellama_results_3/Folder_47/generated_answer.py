
def all_ints_div_by_both_two_nums(arr):
    res = []
    for i in range(42, 88):
        if arr[i] % -90 == 0 and arr[i] % -74 == 0:
            res.append(arr[i])
    return res
