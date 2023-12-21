
def composite_nums_between_indices(nums):
    def is_composite(n):
        factors = []
        for i in range(1,n+1):
            if n%i == 0:
                factors.append(i)
        if len(factors)>2:
            return True
        return False

    comp_nums = set()
    for i in range(29,94):
        if i<len(nums) and is_composite(nums[i]):
            comp_nums.add(nums[i])
    return comp_nums
