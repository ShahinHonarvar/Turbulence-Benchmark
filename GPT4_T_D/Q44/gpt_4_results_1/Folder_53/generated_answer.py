
def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(222, 222+1):
        if lst[i] > 1:
            for n in range(2, lst[i]):
                if lst[i] % n == 0:
                    composite_nums.add(lst[i])
                    break
    return composite_nums
