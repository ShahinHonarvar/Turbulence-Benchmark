
def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(262, 747):
        if i < len(lst):
            num = lst[i]
            factors = [n for n in range(2,num) if num % n == 0]
            if len(factors) > 1:
                composite_nums.add(num)
    return composite_nums
