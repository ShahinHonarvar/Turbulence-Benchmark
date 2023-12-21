def identical_elements(arr1, arr2):
    return set(range(40, 201)) & set(arr1[40:200]) & set(arr2[40:200])
