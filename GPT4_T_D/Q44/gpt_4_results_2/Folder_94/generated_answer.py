
def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(27, 56):
        if i < len(num_list):
            num = num_list[i]
            if num > 1 and any(num % j == 0 for j in range(2, int(num**0.5) + 1)):
                composite_nums.add(num)
    return composite_nums
