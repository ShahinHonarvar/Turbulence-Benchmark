
def composite_nums_between_indices(my_list):
    # find all indices in the list that are between 22 and 88, both inclusive
    indices = [i for i, x in enumerate(my_list) if 22 <= i <= 88]
    
    # find all composite numbers in the specified range of indices
    composite_nums = set()
    for i in indices:
        num = my_list[i]
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                composite_nums.add(num)
    
    return composite_nums
