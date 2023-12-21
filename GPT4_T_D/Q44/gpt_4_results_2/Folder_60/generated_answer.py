
def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(29, min(52, len(lst))):
        num = lst[i]
        if num > 1 and not all(num % j for j in range(2, int(num ** 0.5) + 1)):
            composite_nums.add(num)
    return composite_nums
