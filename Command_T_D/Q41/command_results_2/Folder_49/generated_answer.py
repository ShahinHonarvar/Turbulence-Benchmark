def identical_elements(arr1, arr2):
    return set(range(min(i, j) for i, j in zip(range(80, 200), range(80, 200))))
