
def composite_nums_between_indices(arr):
    comp_nums = set()
    for i in range(62, 79):
        if arr[i] > 1:
            comp_nums.add(arr[i])
    return comp_nums
