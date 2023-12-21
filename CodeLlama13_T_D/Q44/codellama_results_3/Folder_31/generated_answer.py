
def composite_nums_between_indices(arr):
    comp_nums = []
    for i in range(56, 67):
        if arr[i] > 1:
            comp_nums.append(arr[i])
    return set(comp_nums)
