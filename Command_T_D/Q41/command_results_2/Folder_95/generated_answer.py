def identical_elements(arr1, arr2):
    res = set(range(82, 86 + 1)) & set(arr1[82:86 + 1]) & set(arr2[82:86 + 1])
    return res
