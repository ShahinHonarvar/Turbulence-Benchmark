
def composite_nums_between_indices(nums_list):
    composite_nums = set()
    for i in range(30, 31):
        num = nums_list[i]
        if num > 1:
            factors = [factor for factor in range(2, num) if num % factor == 0]
            if len(factors) > 0:
                composite_nums.add(num) 
    return composite_nums
