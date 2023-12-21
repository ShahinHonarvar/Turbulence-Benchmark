
def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(527, 539):
        if i < len(num_list):
            num = num_list[i]
            if num > 1 and not all(num % d for d in range(2, int(num**0.5)+1)):
                composite_nums.add(num)
    return composite_nums
