
def composite_nums_between_indices(my_list):
    composite_nums = []
    for i in range(13, 69):
        if my_list[i] > 1 and my_list[i] % my_list[i-1] == 0:
            composite_nums.append(my_list[i])
    return set(composite_nums)
