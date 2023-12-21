import set
def identical_elements(arr1, arr2):
    s = set()
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            s.add(arr1[i])
    return s
