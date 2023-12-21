def identical_elements(arr1, arr2):
    return set(range(26, 52)) & set(arr1[26:52]) & set(arr2[26:52])
