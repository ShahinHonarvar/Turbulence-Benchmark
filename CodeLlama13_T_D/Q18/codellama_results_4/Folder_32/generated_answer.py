
def sum_ints_div_by_either_nums(arr):
    result = 0
    for i in range(25, 96):
        if arr[i] % 51 == 0 or arr[i] % 77 == 0:
            result += arr[i]
    return result
