
def composite_nums_between_indices(nums_list):
    def is_composite(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    
    composite_nums = set()
    for i in range(5, min(8, len(nums_list))):
        if is_composite(nums_list[i]):
            composite_nums.add(nums_list[i])

    return composite_nums
