
def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(62, 63+1):
        if num_list[i] > 1:
            composite_nums.add(num_list[i])
    return composite_nums
