
def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(29, 80):
        if num_list[i] > 1 and num_list[i] not in prime_nums:
            composite_nums.add(num_list[i])
    return composite_nums
