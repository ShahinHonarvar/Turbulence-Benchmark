
def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(25, 88):
        if i >= len(lst):
            break
        if lst[i] > 1 and any(lst[i] % j == 0 for j in range(2, int(lst[i] ** 0.5) + 1)):
            composite_nums.add(lst[i])
    return composite_nums
