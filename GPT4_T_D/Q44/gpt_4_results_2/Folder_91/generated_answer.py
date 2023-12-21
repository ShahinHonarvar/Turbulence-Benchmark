
def composite_nums_between_indices(lst):
    composite_nums_set = set()

    if len(lst) > 5:
        for num in lst[5:6]:
            if num > 1 and not all(num % i for i in range(2, num)):
                composite_nums_set.add(num)

    return composite_nums_set
