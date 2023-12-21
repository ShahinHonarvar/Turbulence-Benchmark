
def composite_nums_between_indices(lst):
    composite_set = set()
    for i in range(43, 52):
        if i < len(lst):
            num = lst[i]
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        composite_set.add(num)
                        break
    return composite_set
