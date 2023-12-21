
def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(75, 95):
        if i < len(lst) and lst[i] > 1:
            for j in range(2, lst[i]):
                if (lst[i] % j) == 0:
                    composite_nums.add(lst[i])
                    break
    return composite_nums
