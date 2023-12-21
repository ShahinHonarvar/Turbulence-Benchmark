
def composite_nums_between_indices(list_of_ints):
    composite_nums = set()
    for i in range(35, 50):
        if i < len(list_of_ints):
            num = list_of_ints[i]
            if num > 1 and not all(num % i for i in range(2, num)):
                composite_nums.add(num)
    return composite_nums
