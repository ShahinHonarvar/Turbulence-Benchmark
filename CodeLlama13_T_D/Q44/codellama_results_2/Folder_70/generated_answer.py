
def composite_nums_between_indices(arr):
    composites = []
    for i in range(32, 36):
        if arr[i] > 1:
            composites.append(arr[i])
    return set(composites)
