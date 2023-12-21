
def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(686, 988):
        if i < len(num_list):
            num = num_list[i]
            if num > 1 and any(num % i == 0 for i in range(2, num)):
                composite_nums.add(num)
    return composite_nums
