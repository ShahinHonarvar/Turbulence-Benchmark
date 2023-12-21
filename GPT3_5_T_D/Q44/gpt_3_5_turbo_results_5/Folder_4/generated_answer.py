
def composite_nums_between_indices(nums):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False

    composite_nums = set()
    for i in range(56, 99):
        if is_composite(nums[i]):
            composite_nums.add(nums[i])

    return composite_nums
