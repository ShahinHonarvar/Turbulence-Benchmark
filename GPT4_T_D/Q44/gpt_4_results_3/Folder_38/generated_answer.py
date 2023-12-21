
def composite_nums_between_indices(nums):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    composite_nums = set()
    for i in range(29, min(94, len(nums))):
        if is_composite(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums
