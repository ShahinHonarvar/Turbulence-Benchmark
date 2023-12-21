
def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(52, 72):
        if i < len(lst) and not all(lst[i] % n for n in range(2, int(lst[i]**0.5) + 1)):
            composite_nums.add(lst[i])
    return composite_nums
