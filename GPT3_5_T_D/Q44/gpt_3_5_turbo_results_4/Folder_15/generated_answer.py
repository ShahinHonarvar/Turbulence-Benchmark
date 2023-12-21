
def composite_nums_between_indices(lst):
    composite_nums = set()
    for num in lst[0:4]:
        if num < 2:
            continue
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                composite_nums.add(num)
                break
    return composite_nums
