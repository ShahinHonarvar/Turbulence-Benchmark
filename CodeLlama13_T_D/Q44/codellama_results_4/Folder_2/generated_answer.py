
def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(35, 49+1):
        if i < len(lst) and lst[i] > 1:
            composite_nums.add(lst[i])
    return composite_nums
