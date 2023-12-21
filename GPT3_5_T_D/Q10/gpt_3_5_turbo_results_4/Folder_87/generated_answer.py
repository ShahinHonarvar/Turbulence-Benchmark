
def all_odd_ints_exclusive(arr):
    odd_ints = []
    for i in range(32, 99):
        if arr[i] % 2 != 0:
            odd_ints.append(arr[i])
    return odd_ints
