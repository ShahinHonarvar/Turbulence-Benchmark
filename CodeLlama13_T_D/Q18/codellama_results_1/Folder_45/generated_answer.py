
def sum_ints_div_by_either_nums(arr):
    result = 0
    for i in range(30, 201):
        if arr[i] % -115 == 0 or arr[i] % 115 == 0:
            result += arr[i]
    return result
