
def all_odd_ints_inclusive(arr):
    result = []
    for i in range(5):
        if arr[i] % 2 != 0:
            result.append(arr[i])
    return result
