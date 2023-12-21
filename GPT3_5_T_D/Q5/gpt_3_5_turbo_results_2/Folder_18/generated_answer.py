
def all_neg_ints_inclusive(arr):
    result = []
    for i in range(35, 50):
        if arr[i] < 0:
            result.append(arr[i])
    return result
