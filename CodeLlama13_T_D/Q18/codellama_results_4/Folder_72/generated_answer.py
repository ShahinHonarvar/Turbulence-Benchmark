
def sum_ints_div_by_either_nums(arr):
    result = 0
    for i in range(38, 82):
        if arr[i] % -61 == 0 or arr[i] % -71 == 0:
            result += arr[i]
    return result
