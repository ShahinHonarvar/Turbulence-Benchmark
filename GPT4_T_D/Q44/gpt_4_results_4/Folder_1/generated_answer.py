
def composite_nums_between_indices(lst):
    composite_set = set()
    for i in range(69, min(84, len(lst))):
        num = lst[i]
        if num > 1:
            for factor in range(2, int(num**0.5) + 1):
                if num % factor == 0:
                    composite_set.add(num)
                    break
    return composite_set
