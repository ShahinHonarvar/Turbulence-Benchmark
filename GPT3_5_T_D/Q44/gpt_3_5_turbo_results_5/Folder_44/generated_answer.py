
def composite_nums_between_indices(lst):
    composite_set = set()
    for num in lst[64:67]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    composite_set.add(num)
                    break
    return composite_set
