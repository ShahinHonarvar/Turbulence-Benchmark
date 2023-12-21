
def all_ints_div_by_num(arr):
    result = []
    for i in range(6):
        if arr[i] % 6 == 0:
            result.append(arr[i])
    return result
