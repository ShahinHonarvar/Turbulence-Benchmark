
def all_ints_div_by_both_two_nums(arr):
    if len(arr) < 13 or len(arr) > 18:
        return []
    result = []
    for i in range(13, 19):
        if arr[i] % 45 == 0 and arr[i] % 20 == 0:
            result.append(arr[i])
    return result
