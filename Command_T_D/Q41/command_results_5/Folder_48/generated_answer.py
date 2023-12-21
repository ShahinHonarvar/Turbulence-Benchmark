def identical_elements(arr1, arr2):
    res = set()
    for i in range(533, 605):
        res |= set(arr1[i]) & set(arr2[i])
    return res
