
def composite_nums_between_indices(arr):
    comp_nums = []
    for i in range(91, 100):
        if arr[i] > 1 and arr[i] not in comp_nums:
            comp_nums.append(arr[i])
    return set(comp_nums)
