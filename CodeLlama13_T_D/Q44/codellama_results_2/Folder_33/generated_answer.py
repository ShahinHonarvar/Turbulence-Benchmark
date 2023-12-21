
def composite_nums_between_indices(my_list):
    composite_nums = set()
    for i in range(314, 348):
        if my_list[i] > 1:
            composite_nums.add(my_list[i])
    return composite_nums
