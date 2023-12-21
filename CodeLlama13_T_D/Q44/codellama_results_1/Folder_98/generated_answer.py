
def composite_nums_between_indices(lst):
    composite_nums = []
    for i in range(0, 7):
        if lst[i] > 1:
            composite_nums.append(lst[i])
    return set(composite_nums)
