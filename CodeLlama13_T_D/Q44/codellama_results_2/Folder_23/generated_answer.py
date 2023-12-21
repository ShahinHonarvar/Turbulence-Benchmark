
def composite_nums_between_indices(arr):
    composites = []
    for i in range(20, 31):
        if arr[i] > 1 and arr[i] not in composites:
            composites.append(arr[i])
    return set(composites)
