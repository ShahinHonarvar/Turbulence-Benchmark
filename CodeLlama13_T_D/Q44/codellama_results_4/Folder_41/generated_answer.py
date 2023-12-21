
def composite_nums_between_indices(arr):
    composites = set()
    for i in range(3):
        if arr[i] > 1 and arr[i] % arr[i-1] == 0:
            composites.add(arr[i])
    return composites
