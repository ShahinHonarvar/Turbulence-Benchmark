
def composite_nums_between_indices(lst):
    composite_nums_set = set()
    for i in range(40, 81):
        if i < len(lst):
            num = lst[i]
            if num > 1 and not all(num % i for i in range(2, num)):
                composite_nums_set.add(num)
    return composite_nums_set
