 
def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(14, 65):
        num = num_list[i]
        factors = [x for x in range(2, int(num/2)+1) if num % x == 0]
        if len(factors) > 0:
            composite_nums.add(num)
    return composite_nums
