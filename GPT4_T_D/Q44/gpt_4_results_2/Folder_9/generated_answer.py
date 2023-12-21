
def composite_nums_between_indices(nums):
    def is_composite(num):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    return True
            else:
                return False
        else:
            return False
    composite_set = set()
    for i in range(80, 201):
        if i < len(nums) and is_composite(nums[i]):
            composite_set.add(nums[i])
    return composite_set
