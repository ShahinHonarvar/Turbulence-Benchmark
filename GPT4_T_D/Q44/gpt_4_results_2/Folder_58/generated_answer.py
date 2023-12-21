
def composite_nums_between_indices(lst):
    composite_nums = set()
    for idx in range(533, 606):
        if idx < len(lst):
            num = lst[idx]
            if num > 1 and not all(num % i for i in range(2, int(num**0.5) + 1)):
                composite_nums.add(num)
    return composite_nums
