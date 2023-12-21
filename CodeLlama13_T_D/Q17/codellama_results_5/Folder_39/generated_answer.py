
def all_ints_div_by_both_two_nums(arr):
    result = []
    for i in range(13, 77):
        if arr[i] % -66 == 0 and arr[i] % -32 == 0:
            result.append(arr[i])
    return result
