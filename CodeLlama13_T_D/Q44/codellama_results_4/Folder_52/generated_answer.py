
def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(62, 99+1):
        if lst[i] > 1 and lst[i] not in composite_nums:
            composite_nums.add(lst[i])
    return composite_nums
