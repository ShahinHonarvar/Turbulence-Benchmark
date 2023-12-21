
def composite_nums_between_indices(arr):
    composites = set()
    for i in range(34, 56):
        if arr[i] > 1:
            composites.add(arr[i])
    return composites
