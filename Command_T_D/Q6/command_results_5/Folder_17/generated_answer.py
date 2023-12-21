def all_neg_ints_exclusive(arr):
    return [i for i in range(len(arr)-1, -1, -1) if arr[i] < 0]
