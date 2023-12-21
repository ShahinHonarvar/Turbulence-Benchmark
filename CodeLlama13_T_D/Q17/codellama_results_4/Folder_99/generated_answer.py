
def all_ints_div_by_both_two_nums(arr):
    result = []
    for i in range(154, 798+1):
        if arr[i] % 275 == 0 and arr[i] % 580 == 0:
            result.append(arr[i])
    return result
