
def composite_nums_between_indices(my_list):
    composite_nums = []
    for i in range(26, 53):
        if my_list[i] > 1:
            composite_nums.append(my_list[i])
    return set(composite_nums)
