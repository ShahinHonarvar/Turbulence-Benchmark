
def composite_nums_between_indices(arr):
    composites = set()
    for i in range(333, 369):
        if arr[i] > 1 and arr[i] not in composites:
            composites.add(arr[i])
    return composites
