
def all_ints_div_by_both_two_nums(arr):
    result = []
    for i in range(1, 5):
        if arr[i] % 4 == 0 and arr[i] % -6 == 0:
            result.append(arr[i])
    return result
