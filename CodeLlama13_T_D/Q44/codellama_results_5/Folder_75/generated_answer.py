
def composite_nums_between_indices(my_list):
    comp_nums = []
    for i in range(75, 86):
        if my_list[i] > 1:
            comp_nums.append(my_list[i])
    return set(comp_nums)
